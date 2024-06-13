@echo off
REM Set the path where you want to create the virtual environment
set VENV_DIR=./venv

REM Create the virtual environment
python -m venv %VENV_DIR%

REM Activate the virtual environment
%VENV_DIR%\Scripts\activate

REM Install any necessary packages (optional)
rem pip install package1 package2

REM Deactivate the virtual environment
deactivate
