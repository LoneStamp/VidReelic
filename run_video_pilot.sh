#!/bin/bash

PYTHON_SCRIPT="main.py"

python3 --version &> /dev/null
if [ $? -ne 0 ]; then
  echo "Python 3 is not installed. Please install it first."
  exit 1
fi


if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "Error: $PYTHON_SCRIPT not found!"
  exit 1
fi

echo "Running the Python script $PYTHON_SCRIPT..."
python3 "$PYTHON_SCRIPT"

if [ $? -eq 0 ]; then
  echo "Python script ran successfully!"
else
  echo "Error: Python script did not run successfully."
  exit 1
fi
