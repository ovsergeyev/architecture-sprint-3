# Запуск локального сервера
  uvicorn main:app --reload

# Создание и применение миграций
- alembic revision --autogenerate -m "Initial migration"
- alembic upgrade head
- alembic history --verbose