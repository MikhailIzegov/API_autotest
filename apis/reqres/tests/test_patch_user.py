import jsonschema
import requests

from apis.reqres.utils.read_json import load_schema


def test_patch_user():
    response = requests.patch(url='https://reqres.in/api/users/3', json={
            "name": "morpheus666"
    })

    schema = load_schema('patch_users.json')
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)
