# Используем официальный образ Python
FROM python:3.8


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app


COPY requirements.txt /app/


RUN pip install -r requirments.txt

COPY . /app/


CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]