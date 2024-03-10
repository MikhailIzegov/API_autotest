import jsonschema
import requests

from apis.reqres.utils.read_json import load_schema


def test_get_users_status_code():
    response = requests.get(url='https://reqres.in/api/users')

    assert response.status_code == 200


def test_get_users_per_page():
    response = requests.get(url='https://reqres.in/api/users', params={'per_page': 1})

    assert len(response.json()['data']) == 1
    assert response.json()['per_page'] == 1


def test_headers():
    response = requests.get(url='https://reqres.in/api/users', headers={'Connection': 'keep-alive'})

    assert 'Connection' in response.headers
    assert response.headers['Connection'] == 'keep-alive'


def test_post_user():
    response = requests.post(url='https://reqres.in/api/users', json={
            "name": "morpheus",
            "job": "leader"
    }
                             )
    # assert response.json()['name'] == 'morpheus'
    # assert response.json()['job'] == 'leader'

    # Валидация схемы
    schema = load_schema('post_users.json')
    assert response.status_code == 201
    jsonschema.validate(response.json(), schema)


def test_put_user():
    response = requests.put(url='https://reqres.in/api/users/3', json={
            "name": "morpheus555",
            "job": "zion resident"
    })

    schema = load_schema('put_users.json')
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)


def test_delete_user():
    user_to_delete = 3
    response = requests.delete(url=f'https://reqres.in/api/users/{user_to_delete}')

    assert response.status_code == 204


def test_patch_user():
    response = requests.patch(url='https://reqres.in/api/users/3', json={
            "name": "morpheus666"
    })

    schema = load_schema('patch_users.json')
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)
