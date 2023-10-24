#!/bin/bash

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install Python 3 before running this script."
    exit 1
fi

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install project dependencies from requirements.txt
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

echo "Installation complete. To activate the virtual environment, run: source venv/bin/activate"
