@echo off

REM Create a virtual environment
virtualenv virtualenv

REM Activate the virtual environment
call virtualenv\Scripts\activate

REM Install packages from requirements.txt
pip install -r requirements.txt

REM Deactivate the virtual environment
deactivate
