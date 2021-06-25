FROM python:3.9-alpine as base

ARG CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev make
RUN pip install poetry
COPY . /service
WORKDIR /service
RUN python -m venv /service/env && . /service/env/bin/activate && poetry install && poetry build

COPY ./docker/file_proxy/start.sh /service/start.sh
RUN chmod +x /service/start.sh

CMD /service/start.sh