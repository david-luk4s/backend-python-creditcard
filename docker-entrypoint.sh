#!/bin/bash

sleep 3

# Start Gunicorn processes

echo Starting Gunicorn

exec gunicorn main:app --bind 0.0.0.0:8080 --workers 4