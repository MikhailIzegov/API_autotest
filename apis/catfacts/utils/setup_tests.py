import json
import allure
from allure import attachment_type
from curlify import to_curl
from requests import sessions


def catfact_api(method, url, **kwargs):
    base_url = 'https://catfact.ninja'
    new_url = base_url + url
    method = method.upper()
    with allure.step(f'{method} {url}'):
        with sessions.Session() as session:
            response = session.request(method=method, url=new_url, **kwargs)
            message = to_curl(response.request)
            allure.attach(body=message.encode('utf8'), name='curl',
                          attachment_type=attachment_type.TEXT, extension='txt')
            allure.attach(body=json.dumps(response.json(), indent=4).encode('utf8'), name='Response JSON',
                          attachment_type=attachment_type.JSON, extension='json')
    return response
