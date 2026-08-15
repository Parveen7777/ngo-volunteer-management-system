#!/bin/sh

echo "Starting NGO Volunteer Management System..."

# Create database folder if it does not exist
mkdir -p database

# Run the Flask application
python app.py
