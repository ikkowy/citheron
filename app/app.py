import logging
import logging.handlers
import os
import sys
import time
import re

import argon2
import jwt
import sqlalchemy
import yaml

from flask import Flask, request, Response, abort
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth
from werkzeug.exceptions import HTTPException

import schema
from version import CITHERON_VERSION

################################################################################
### Load the configuration file

CITHERON_CONFIG_FILE = os.getenv("CITHERON_CONFIG_FILE")

if CITHERON_CONFIG_FILE is None:
    raise Exception("missing environment variable 'CITHERON_CONFIG_FILE'")

config = yaml.safe_load(open(CITHERON_CONFIG_FILE, "r"))

CITHERON_DATABASE_HOST = config["database"]["host"]
CITHERON_DATABASE_PORT = config["database"]["port"]
CITHERON_DATABASE_DBNAME = config["database"]["dbname"]
CITHERON_DATABASE_USER = config["database"]["user"]
CITHERON_DATABASE_PASSWORD = config["database"]["password"]

CITHERON_LOG_FILE = config.get("log", {}).get("file")
CITHERON_LOG_LEVEL = config.get("log", {}).get("level", "info")

CITHERON_JWT_KEY = config["jwtKey"]

################################################################################
### Setup the logging system

def log_level(level):
    return {
        None : logging.INFO,
        "debug" : logging.DEBUG,
        "info" : logging.INFO,
        "warning" : logging.WARNING,
        "error" : logging.ERROR,
        "critical" : logging.CRITICAL
    }[level]

logger = logging.getLogger("citheron")
logger.setLevel(log_level(CITHERON_LOG_LEVEL))

formatter = logging.Formatter("%(asctime)s %(name)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%dT%H:%M:%S%z")

logConsoleHandler = logging.StreamHandler()
logConsoleHandler.setFormatter(formatter)
logConsoleHandler.setLevel(log_level(CITHERON_LOG_LEVEL))
logger.addHandler(logConsoleHandler)

CITHERON_LOG_FILE = os.getenv("CITHERON_LOG_FILE")
if CITHERON_LOG_FILE is not None:
    logFileHandler = logging.FileHandler(CITHERON_LOG_FILE)
    logFileHandler.setFormatter(formatter)
    logFileHandler.setLevel(log_level(CITHERON_LOG_LEVEL))
    logger.addHandler(logFileHandler)

################################################################################

app = Flask(__name__)

uri = f"postgresql+psycopg2://{CITHERON_DATABASE_USER}:{CITHERON_DATABASE_PASSWORD}@{CITHERON_DATABASE_HOST}:{CITHERON_DATABASE_PORT}/{CITHERON_DATABASE_DBNAME}"

engine = sqlalchemy.create_engine(uri)

session = sqlalchemy.orm.Session(engine)

pwhasher = argon2.PasswordHasher()

################################################################################
### Helper functions

def get_unix_time():
    return int(time.time())

def argon2_verify(hash, password):
    try:
        pwhasher.verify(hash, password)
    except:
        return False
    return True

def check_user_credentials(username, password):
    query = session.query(schema.User).filter_by(name=username)
    if query.count() == 0: return False
    entry = query.first()
    if not entry.enabled: return False
    return argon2_verify(entry.pwhash, password)

def is_admin(username):
    admins = ["admin"]
    return username in admins

def check_email(email):
    if len(email.encode('utf-8')) > 254: return False
    return bool(re.match(r"^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,}$", email))

################################################################################

# Check if there is a database version conflict
if not sqlalchemy.inspect(engine).has_table("registry"):
    raise Exception("database table 'registry' not found")
result = session.query(schema.Registry).filter_by(key="citheron.version")
if result.count() == 0 or result.first().value != CITHERON_VERSION:
    raise Exception("database version conflict")

################################################################################

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme="Bearer")
multi_auth = MultiAuth(basic_auth, token_auth)

################################################################################

@basic_auth.verify_password
def verify_password(username, password):
    if check_user_credentials(username, password):
        return username

@token_auth.verify_token
def verify_token(token):
    try:
        payload = jwt.decode(token, CITHERON_JWT_KEY, algorithms=["HS256"])
        if payload["exp"] < get_unix_time():
            return False
        return payload["username"]
    except:
        return False

@app.route("/api/v1/tokens", methods=["GET"])
@basic_auth.login_required
def api_v1_tokens():
    if request.method == "GET":
        return Response(jwt.encode(
            {
                "exp" : get_unix_time() + 3600, # ticket expires in one hour
                "username" : basic_auth.current_user()
            },
            CITHERON_JWT_KEY, algorithm="HS256"
        ), status=200, mimetype="text/plain") # OK

@app.route("/api/v1/users", methods=["POST"])
@multi_auth.login_required
def api_v1_users():
    if request.method == "POST":
        if request.mimetype == "application/json":
            if is_admin(multi_auth.current_user()):

                if "name" not in request.json:
                    return Response("Missing required user name.", status=400, mimetype="text/plain") # Bad Request

                name = request.json["name"]

                # Check if user name is already used
                if session.query(schema.User).filter_by(name=name).count() != 0:
                    return Response("User name is already used.", status=409, mimetype="text/plain") # Conflict

                firstname = request.json.get("firstname")

                lastname = request.json.get("lastname")

                email = request.json.get("email")

                if email is not None:

                    email = email.lower()

                    # Check if email address is already used
                    if session.query(schema.User).filter_by(email=email).count() != 0:
                        return Response("Email address is already used.", status=409, mimetype="text/plain") # Conflict

                    if not check_email(email):
                        return Response("Malformed email address.", status=400, mimetype="text/plain") # Bad Request

                password = request.json.get("password")

                pwhash = None
                if password is not None:
                    pwhash = pwhasher.hash(password)

                enabled = request.json.get("enabled", True)

                # Add user entry in database
                user = schema.User(name=name, firstname=firstname, lastname=lastname, email=email, pwhash=pwhash, enabled=True)
                session.add(user)
                session.commit()

                return Response("A new user has been successfully created.", status=201, mimetype="text/plain") # Created

            else:
                return Response("You need to be admin for this operation.", status=401, mimetype="text/plain") # Unauthorized
        else:
            abort(415) # Unsupported Media Type

################################################################################

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return Response(f"{e.code} {e.name}", status=e.code, mimetype="text/plain")

@basic_auth.error_handler
@token_auth.error_handler
def token_auth_error(status):
    return Response(f"Access denied.", status=status, mimetype="text/plain")
