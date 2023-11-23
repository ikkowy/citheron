#!/bin/bash

cd /opt/citheron

if [ ! -d env ]; then
    python3 -m venv env
fi

env/bin/pip3 install -r requirements.txt

env/bin/python3 -c '
from app import app
from model import db
with app.app_context():
    db.create_all()
'

env/bin/flask run --debug --host=0.0.0.0 &

FLASK_PID="$!"

trap "kill $FLASK_PID" exit INT TERM

wait
