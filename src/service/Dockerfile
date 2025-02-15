FROM python:3.9-slim

WORKDIR /usr/src/app

COPY req.txt req.txt

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && pip install --upgrade pip \
    && pip install -r req.txt


COPY . .
COPY ./script.sh /usr/bin
RUN chmod +x /usr/bin/script.sh

CMD ["sh", "/usr/bin/script.sh"]