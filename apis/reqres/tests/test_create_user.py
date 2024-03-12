import jsonschema
import requests

from apis.reqres.utils.read_json import load_schema


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
