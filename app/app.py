import logging
import logging.handlers
import os
import sys
import time
import re

from flask import Flask, request, Response, abort
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import HTTPException
import jwt

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

auth = HTTPTokenAuth(scheme="Bearer")

def get_unix_time():
    return int(time.time())

@auth.verify_token
def verify_token(token):
    try:
        payload = jwt.decode(token, CITHERON_JWT_KEY, algorithms=["HS256"])
        if payload["exp"] < get_unix_time():
            return False
        return payload["username"]
    except:
        return False

def check_user_credentials(username, password):
    if username == "helga" and password == "secret": return True
    return False

def is_admin(username):
    admins = ["helga"]
    if username in admins: return True
    return False

def check_email(email):
    if len(email.encode('utf-8')) > 254: return False
    return bool(re.match(r"^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,}$", email))

@app.route("/api/v1/tokens", methods=["POST"])
def api_v1_tokens():
    if request.method == "POST":
        if request.mimetype == "application/json":
            if check_user_credentials(request.json["username"], request.json["password"]):
                return Response(jwt.encode(
                    {
                        "exp" : get_unix_time() + 3600, # ticket expires in one hour
                        "username" : "helga"
                    },
                    CITHERON_JWT_KEY,
                    algorithm="HS256"
                ), mimetype="text/plain")
            else:
                abort(401) # Unauthorized
        else:
            abort(415) # Unsupported Media Type

@app.route("/api/v1/users", methods=["POST"])
@auth.login_required
def api_v1_users():
    if request.method == "POST":
        if request.mimetype == "application/json":
            if is_admin(auth.current_user()):

                if "name" not in request.json:
                    return Response("Missing required user name.", status=400, mimetype="text/plain") # Bad Request

                name = request.json["name"]

                # Check if user name is already used
                if db.session.query(model.user).filter_by(name=name).count() != 0:
                    return Response("User name already exists.", status=409, mimetype="text/plain") # Conflict

                firstname = request.json.get("firstname")

                lastname = request.json.get("lastname")

                if "email" not in request.json:
                    return Response("Missing required email address.", status=400, mimetype="text/plain") # Bad Request

                email = request.json["email"].lower()

                # Check if email is already used
                if db.session.query(model.user).filter_by(email=email).count() != 0:
                    return Response("Email address already exists.", status=409, mimetype="text/plain") # Conflict

                if not check_email(email):
                    return Response("Malformed email address.", status=400, mimetype="text/plain") # Bad Request

                enabled = request.json.get("enabled", True)

                # Add user entry in database
                user = model.user(name=name, firstname=firstname, lastname=lastname, email=email, enabled=True)
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

@auth.error_handler
def auth_error(status):
    return Response(f"Access denied.", status=status, mimetype="text/plain")

@app.route("/")
def index():
    logger.info("Hello world!")
    return "Hello world!"

@app.route("/secret")
@auth.login_required
def secret():
    return "Secret stuff!"
