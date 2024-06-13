#!/bin/bash
# Set the path to your virtual environment
VENV_DIR="venv"

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Run your Python program (replace with the actual path to your program)
python -m src.blackjack.main

# Deactivate the virtual environment (optional)
deactivate

