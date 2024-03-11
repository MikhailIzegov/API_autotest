import datetime

import jsonschema
import pytest
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


@pytest.mark.parametrize('per_page', [6, 12, 11, 13, 3, 4, 24])
def test_users_list_total_pages_count(per_page):
    def expected_total_pages(total, per_page_numb):
        if total <= per_page_numb:
            exp_total_pages = 1
        elif total % per_page_numb == 0:
            exp_total_pages = total // per_page_numb
        else:
            exp_total_pages = total // per_page_numb + 1
        return exp_total_pages

    response = requests.get(url='https://reqres.in/api/users', params={'per_page': per_page})
    resp_total = response.json()['total']

    assert response.json()['total_pages'] == expected_total_pages(resp_total, per_page)


def test_update_user_datetime():
    today_utc = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M')
    response = requests.put(
        url='https://reqres.in/api/users/3',
        json={'name': 'student_name_1', 'job': 'job_name'}
    )

    assert response.status_code == 200
    assert response.json()['updatedAt'][:-8] == today_utc  # Проверка с текущим временем до минуты


def test_error_email_register_new_user():
    response = requests.post(
        url='https://reqres.in/api/register',
        json={
            "password": "morpheus_password"
        }
                             )
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing email or username'


def test_error_password_register_new_user():
    response = requests.post(
        url='https://reqres.in/api/register',
        json={
            "email": "morpheus@example.com"
        }
                             )
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'
