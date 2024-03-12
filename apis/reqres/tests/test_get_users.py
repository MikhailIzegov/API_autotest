import pytest
import requests


def test_get_users_status_code():
    response = requests.get(url='https://reqres.in/api/users')

    assert response.status_code == 200


def test_get_users_per_page():
    response = requests.get(url='https://reqres.in/api/users', params={'per_page': 1})

    assert len(response.json()['data']) == 1
    assert response.json()['per_page'] == 1


def test_get_users_header():
    response = requests.get(url='https://reqres.in/api/users', headers={'Connection': 'keep-alive'})

    assert 'Connection' in response.headers
    assert response.headers['Connection'] == 'keep-alive'


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
