# Используем официальный образ Debian
FROM debian:bullseye-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# CMD ["celery", "-A", "celery.app", "worker", "--loglevel=info"]
