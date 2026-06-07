#!/bin/bash
# Create venv
python3 -m venv venv

# Activate venv
if [[ "$OSTYPE" == "msys" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Install requirements
pip install python-telegram-bot[job-queue] beautifulsoup4 requests python-dotenv
