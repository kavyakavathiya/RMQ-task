#!/bin/bash

set -e

# Start the Django server in the background
python3 manage.py runserver 0.0.0.0:8000 &

# Start the worker process in the foreground
python3 /app-backend-worker/tasks/worker.py
