import requests

def get_weather_data(url, payload):
    response = requests.get(url, payload)
    return response

if __name__ == '__main__':
    url = 'https://wttr.in'
    payload = '/san%20francisco?nTqu&lang=en'

    response = get_weather_data(url, payload)
    response.raise_for_status()

    print(response.text)