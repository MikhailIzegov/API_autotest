import random
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


def test_get_list_of_facts():
    response = catfact_api(
        'get',
        url='/facts'
    )

    schema = load_schema('get_list_of_facts.json')
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)


def test_get_list_of_facts_with_params():
    max_length = random.randint(30, 90)
    limit = random.randint(3, 15)
    response = catfact_api(
        'get',
        url='/facts',
        params={'max_length': max_length, 'limit': limit}
    )

    schema = load_schema('get_list_of_facts.json')
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)
    for item in response.json()['data']:
        assert item['length'] <= max_length, f'Длина {item["length"]} превышает максимальное значение {max_length}'
