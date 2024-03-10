import json
import jsonschema
import allure
from allure import attachment_type
import jsonschema
import requests
from curlify import to_curl
from requests import sessions

from apis.catfacts.utils.read_json import load_schema


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


def test_get_all_breeds():
    response = catfact_api(
        'get',
        url='/breeds',
    )

    assert response.status_code == 200


def test_get_breeds_with_limit():
    limit = 2
    response = catfact_api(
        'get',
        url='/breeds',
        params={'limit': limit}
    )
    schema = load_schema('get_all_breeds.json')
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)
    assert response.json()['per_page'] == '2'

# def test_get_users_per_page():
#     response = requests.get(url='https://reqres.in/api/users', params={'per_page': 1})
#
#     assert len(response.json()['data']) == 1
#     assert response.json()['per_page'] == 2


# def test_headers():
#     response = requests.get(url='https://reqres.in/api/users', headers={'Connection': 'keep-alive'})
#
#     assert 'Connection' in response.headers
#     assert response.headers['Connection'] == 'keep-alive'
#
#
# def test_post_user():
#     response = requests.post(url='https://reqres.in/api/users', json={
#             "name": "morpheus",
#             "job": "leader"
#     }
#                              )
#     # assert response.json()['name'] == 'morpheus'
#     # assert response.json()['job'] == 'leader'
#
#     # Валидация схемы
#     schema = load_schema('post_users.json')
#     assert response.status_code == 201
#     jsonschema.validate(response.json(), schema)
#
#
# def test_put_user():
#     response = requests.put(url='https://reqres.in/api/users/3', json={
#             "name": "morpheus555",
#             "job": "zion resident"
#     })
#
#     schema = load_schema('put_users.json')
#     assert response.status_code == 200
#     jsonschema.validate(response.json(), schema)
#
#
# def test_delete_user():
#     user_to_delete = 3
#     response = requests.delete(url=f'https://reqres.in/api/users/{user_to_delete}')
#
#     assert response.status_code == 204
#
#
# def test_patch_user():
#     response = requests.patch(url='https://reqres.in/api/users/3', json={
#             "name": "morpheus666"
#     })
#
#     schema = load_schema('get_all_breeds.json')
#     assert response.status_code == 200
#     jsonschema.validate(response.json(), schema)
#