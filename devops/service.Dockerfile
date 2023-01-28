FROM python:3.9-slim

ENV TZ="America/Bogota"

WORKDIR /global_api

COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt && rm -rf /requirements

COPY . /global_api
WORKDIR /global_api
EXPOSE 80
ENTRYPOINT python3 -m gunicorn --workers=3 --threads=3 config.asgi --bind 0.0.0.0:80 -k uvicorn.workers.UvicornWorker --timeout 360
