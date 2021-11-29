import json
import requests


def handler(event, contexts):
    print('event: {}'.format(json.dumps(event)))

    response = requests.get('https://httpbin.org/get')

    return {
        'status.Code': response.status_code,
        'body': response.json()
    }
