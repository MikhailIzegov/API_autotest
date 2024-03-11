import jsonschema
from apis.catfacts.utils.read_json import load_schema
from apis.catfacts.utils.setup_tests import catfact_api


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
    assert response.json()['per_page'] == str(limit)
