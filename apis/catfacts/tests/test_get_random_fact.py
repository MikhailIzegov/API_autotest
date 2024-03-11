import jsonschema
import random
from apis.catfacts.utils.read_json import load_schema
from apis.catfacts.utils.setup_tests import catfact_api


def test_get_random_fact():
    response = catfact_api(
        'get',
        url='/fact'
    )

    schema = load_schema('get_random_fact.json')
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)


def test_get_random_fact_with_max_length():
    max_length = random.randint(30, 90)
    response = catfact_api(
        'get',
        url='/fact',
        params={'max_length': max_length}
    )

    schema = load_schema('get_random_fact.json')
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)
    assert response.json()['length'] <= max_length
