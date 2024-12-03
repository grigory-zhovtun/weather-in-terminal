import requests
from urllib.parse import urljoin

def fetch_weather_data(location, params=None):
    url = urljoin('https://wttr.in', location)
    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.text

if __name__ == '__main__':
    locations = ['Лондон', 'svo', 'Череповец']
    payload = {
        'lang': 'ru',
        'nTqM': ''
    }

    for location in locations:
        try:
            weather_in_current_location = fetch_weather_data(location, payload)
        except requests.exceptions.HTTPError as e:
            exit("Can't fetch weather data for '{}': {}".format(location, e))

        print(weather_in_current_location)
        print('='*60)