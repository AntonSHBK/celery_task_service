import requests
import os
from app.celery import celery_app

TRANSLATE_SINGLE_URL = os.getenv("TRANSLATE_SINGLE_URL", "http://translate-service:8000/api/translate_single")
TRANSLATE_BATCH_URL = os.getenv("TRANSLATE_BATCH_URL", "http://translate-service:8000/api/translate")

@celery_app.task(name="translate.single")
def translate_single_task(text: str, source_lang: str, target_lang: str):
    """
    Задача для перевода одного текста на один язык.

    :param text: Текст для перевода
    :param source_lang: Язык исходного текста
    :param target_lang: Язык перевода
    :return: Результат перевода
    """
    payload = {
        "text": text,
        "source_lang": source_lang,
        "target_lang": target_lang
    }
    try:
        response = requests.post(TRANSLATE_SINGLE_URL, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@celery_app.task(name="translate.batch")
def translate_batch_task(texts: list, source_lang: str, target_langs: list):
    """
    Задача для пакетного перевода.

    :param texts: Список текстов для перевода
    :param source_lang: Язык исходных текстов
    :param target_langs: Список целевых языков
    :return: Список словарей с результатами перевода
    """
    payload = {
        "texts": texts,
        "source_lang": source_lang,
        "target_langs": target_langs
    }
    try:
        response = requests.post(TRANSLATE_BATCH_URL, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
