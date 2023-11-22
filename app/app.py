import logging
import logging.handlers
import os
import sys

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth

import jwt

logLevelMap = {
    "debug" : logging.DEBUG,
    "info" : logging.INFO,
    "warning" : logging.WARNING,
    "error" : logging.ERROR,
    "critical" : logging.CRITICAL
}

CITHERON_LOG_LEVEL = logLevelMap.get(os.environ.get("CITHERON_LOG_LEVEL", "info"))

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

db = SQLAlchemy(app)

auth = HTTPTokenAuth(scheme="Bearer")

class user(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(254))
    enabled = db.Column(db.Boolean)

@app.route("/api/v1/tokens", methods=["POST"])
def api_v1_tokens():
    if request.method == "POST":
        if request.mimetype == "application/json":
            if request.json["username"] == "helga" and request.json["password"] == "bzzz":
                return jwt.encode({"username" : "helga"}, CITHERON_JWT_KEY, algorithm="HS256")
    return "error"

@app.route("/")
def index():
    logger.info("Hello world!")
    return "Hello world!"
