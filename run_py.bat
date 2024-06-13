@echo off
set VENV_DIR=./venv
call %VENV_DIR%\Scripts\activate

REM Run your Python program
python -m src.blackjack.main

REM Deactivate the virtual environment (optional)
call %VENV_DIR%\Scripts\deactivate


