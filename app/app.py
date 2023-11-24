import logging
import logging.handlers
import os
import sys
import time
import re

from flask import Flask, request, Response, abort
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth
from werkzeug.exceptions import HTTPException
import jwt
import argon2

import model
from model import db

logLevelMap = {
    "debug" : logging.DEBUG,
    "info" : logging.INFO,
    "warning" : logging.WARNING,
    "error" : logging.ERROR,
    "critical" : logging.CRITICAL
}

CITHERON_LOG_LEVEL = logLevelMap[os.environ.get("CITHERON_LOG_LEVEL", "info")]

logger = logging.getLogger("citheron")
logger.setLevel(CITHERON_LOG_LEVEL)

formatter = logging.Formatter("%(asctime)s %(name)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%dT%H:%M:%S%z")

logConsoleHandler = logging.StreamHandler()
logConsoleHandler.setFormatter(formatter)
logConsoleHandler.setLevel(CITHERON_LOG_LEVEL)
logger.addHandler(logConsoleHandler)

CITHERON_LOG_FILE = os.getenv("CITHERON_LOG_FILE")
if CITHERON_LOG_FILE is not None:
    logFileHandler = logging.FileHandler(CITHERON_LOG_FILE)
    logFileHandler.setFormatter(formatter)
    logFileHandler.setLevel(CITHERON_LOG_LEVEL)
    logger.addHandler(logFileHandler)

CITHERON_DATABASE_HOST = os.environ["CITHERON_DATABASE_HOST"]
CITHERON_DATABASE_PORT = os.environ["CITHERON_DATABASE_PORT"]
CITHERON_DATABASE_DBNAME = os.environ["CITHERON_DATABASE_DBNAME"]
CITHERON_DATABASE_USER = os.environ["CITHERON_DATABASE_USER"]
CITHERON_DATABASE_PASSWORD = os.environ["CITHERON_DATABASE_PASSWORD"]

CITHERON_JWT_KEY = os.environ["CITHERON_JWT_KEY"]

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{CITHERON_DATABASE_USER}:{CITHERON_DATABASE_PASSWORD}@{CITHERON_DATABASE_HOST}:{CITHERON_DATABASE_PORT}/{CITHERON_DATABASE_DBNAME}"

db.init_app(app)

pwhasher = argon2.PasswordHasher()

def get_unix_time():
    return int(time.time())

def argon2_verify(hash, password):
    try:
        pwhasher.verify(hash, password)
    except:
        return False
    return True

def check_user_credentials(username, password):
    query = db.session.query(model.user).filter_by(name=username)
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

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme="Bearer")
multi_auth = MultiAuth(basic_auth, token_auth)

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
                if db.session.query(model.user).filter_by(name=name).count() != 0:
                    return Response("User name is already used.", status=409, mimetype="text/plain") # Conflict

                firstname = request.json.get("firstname")

                lastname = request.json.get("lastname")

                email = request.json.get("email")

                if email is not None:

                    email = email.lower()

                    # Check if email address is already used
                    if db.session.query(model.user).filter_by(email=email).count() != 0:
                        return Response("Email address is already used.", status=409, mimetype="text/plain") # Conflict

                    if not check_email(email):
                        return Response("Malformed email address.", status=400, mimetype="text/plain") # Bad Request

                password = request.json.get("password")

                pwhash = None
                if password is not None:
                    pwhash = pwhasher.hash(password)

                enabled = request.json.get("enabled", True)

                # Add user entry in database
                user = model.user(name=name, firstname=firstname, lastname=lastname, email=email, pwhash=pwhash, enabled=True)
                db.session.add(user)
                db.session.commit()

                return Response("A new user has been successfully created.", status=201, mimetype="text/plain") # Created

            else:
                return Response("You need to be admin for this operation.", status=401, mimetype="text/plain") # Unauthorized
        else:
            abort(415) # Unsupported Media Type

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return Response(f"{e.code} {e.name}", status=e.code, mimetype="text/plain")

@basic_auth.error_handler
@token_auth.error_handler
def token_auth_error(status):
    return Response(f"Access denied.", status=status, mimetype="text/plain")
