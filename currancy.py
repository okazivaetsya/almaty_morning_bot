import json
import os

import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

CURRENCY_KEY = os.getenv('CURRENCY_KEY')

url = 'https://api.apilayer.com/currency_data/convert'


def get_currancy_rate(currency_from: str, currency_to: str) -> float:
    """Получаем актуальный курс валюты RUB -> KZT"""
    payload = {}
    params = {
        'apikey': CURRENCY_KEY,
        'to': currency_to,
        'from': currency_from,
        'amount': '1'
    }
    response = requests.get(url, params=params, data=payload)
    json_data = json.loads(response.text)
    return round(json_data['result'], 2)
