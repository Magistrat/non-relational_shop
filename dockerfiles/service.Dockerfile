FROM python:3.10-slim
ENV TZ=Europe/Moscow
WORKDIR /app
COPY .. /app
RUN apt-get update
RUN pip install --upgrade pip && pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-cache --without dev
CMD ["gunicorn", "main:app", "--workers", "3", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "--timeout", "600"]
