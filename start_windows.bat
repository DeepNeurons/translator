@echo off
cd /d %~dp0
call env\Scripts\activate.bat
set FLASK_APP=app.py
flask run