import requests

def get_weather_data(place, params=None):
    url = f'https://wttr.in/{place}'
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text

# Для Лондона
# Для аэропорта Шереметьево
# Для Череповца



if __name__ == '__main__':
    places = ['Лондон', 'svo', 'Череповец']
    payload = {
        'lang': 'ru',
        'nTq': ''
    }
    for place in places:
        response = get_weather_data(place, payload)
        print(response)
        print('='*60)