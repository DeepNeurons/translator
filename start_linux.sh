#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
export FLASK_APP=app.py
flask run

