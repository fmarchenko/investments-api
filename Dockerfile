FROM python:3-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir --src /usr/local/src/ -r requirements.txt
COPY ./investments-api .
COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
