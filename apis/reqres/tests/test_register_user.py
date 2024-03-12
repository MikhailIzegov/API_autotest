import jsonschema
import requests
from apis.reqres.utils.read_json import load_schema


def test_successful_register_user():
    response = requests.post(
        url='https://reqres.in/api/register',
        json={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
    )
    schema = load_schema('register_user.json')
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)


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
