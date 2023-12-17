FROM python:3.11-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY pyproject.toml $APP_HOME/pyproject.toml
COPY poetry.lock $APP_HOME/poetry.lock

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --only main

COPY . .

EXPOSE 5000

CMD ["python", "address_book/address_book.py"]
LABEL maintainer="vskesha@gmail.com"