FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip3 install poetry
RUN poetry install
RUN poetry run playwright install
RUN poetry run playwright install-deps

VOLUME /app/tracing

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]