# Celery Translation Task Queue

Проект представляет собой **шаблон микросервиса обработки задач**, основанный на очередях Celery и Redis.

### Основан на проекте перевода текста:
> [language_translator_M2M100 (GitHub)](https://github.com/AntonSHBK/language_translator_M2M100)

---

## Архитектура

Сервис состоит из трёх частей:

- `translate_service` — API-сервис FastAPI с моделью перевода (M2M100).
- `task_service` — Celery worker, обрабатывающий задачи перевода.
- `Redis` — брокер очередей.

Все сервисы работают в единой Docker-сети.

---

## Запуск

### 1. Клонируй проект

```bash
git clone https://github.com/AntonSHBK/celery_task_service.git
cd celery_task_service
```

### 2. Запусти всё через Docker Compose

```bash
docker-compose up --build
```

> Убедись, что `.env` лежит рядом с `docker-compose.yml`.

## Как использовать как шаблон

1. Замени модель перевода своей (например, генератор, классификатор)
2. Адаптируй `translate_handler.py` и `task_service/`
3. Раздели очередь по типу задач, если нужно
4. Разворачивай как прод- или dev-сервис
