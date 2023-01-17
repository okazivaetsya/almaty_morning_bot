import json
import os

import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

ACCWEATHER_KEY = os.getenv('ACCWEATHER_KEY')

url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/222191'

payload = {}
params = {
    'apikey': ACCWEATHER_KEY,
    'language': 'ru',
    'metric': 'true',
    'details': 'true'
}


def get_forecast():
    """
    Получаем прогноз погоды на день и формируем сообщение
    """
    response = requests.get(url, params=params, data=payload)
    json_data = json.loads(response.text)
    text = json_data[
        'Headline'
    ]['Text']
    day_precipitation = json_data['DailyForecasts'][0][
        'Day'
    ]['PrecipitationProbability']
    day_precipitation_type = json_data['DailyForecasts'][0][
        'Day'
    ]['IconPhrase']
    day_wind = json_data['DailyForecasts'][0][
        'Day'
    ]['Wind']['Speed']['Value']
    night_precipitation = json_data['DailyForecasts'][0][
        'Night'
    ]['PrecipitationProbability']
    night_precipitation_type = json_data['DailyForecasts'][0][
        'Night'
    ]['IconPhrase']
    night_wind = json_data['DailyForecasts'][0][
        'Night'
    ]['Wind']['Speed']['Value']
    rf_temp_min = json_data['DailyForecasts'][0][
        'RealFeelTemperatureShade'
    ]['Minimum']['Value']
    rf_temp_max = json_data['DailyForecasts'][0][
        'RealFeelTemperatureShade'
    ]['Maximum']['Value']
    return (
        f'Погода в Алматы:\n'

        f'Днем {day_precipitation_type.lower()}, '
        f'(вероятность осадков – {day_precipitation}%), '
        f'ветер {day_wind} км/ч\n'

        f'Ночью {night_precipitation_type.lower()}, '
        f'(вероятность осадков – {night_precipitation}%), '
        f'ветер {night_wind} км/ч\n'

        f'Температура от {round(rf_temp_min)} до {round(rf_temp_max)}\n'
        f'Примечание: {text}\n'
    )
