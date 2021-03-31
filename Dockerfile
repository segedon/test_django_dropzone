FROM python:3.6
ENV PYTHONUNBUFFERED=1
RUN pip install poetry
RUN mkdir /code
COPY . /code
WORKDIR /code
RUN poetry install && poetry run python manage.py migrate
ENTRYPOINT poetry run python manage.py runserver 0.0.0.0:8080
