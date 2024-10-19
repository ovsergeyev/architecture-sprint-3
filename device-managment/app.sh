#!/bin/bash

# alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

# gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
gunicorn --access-logfile - --error-logfile - --log-level debug  main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000