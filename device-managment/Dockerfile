FROM python:3.9

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /app.sh

# RUN alembic upgrade head
#CMD ["alembic", "upgrade", "head"]
#CMD ["gunicorn", "main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]