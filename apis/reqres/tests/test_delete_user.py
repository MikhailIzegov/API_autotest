import requests


def test_delete_user():
    user_to_delete = 3
    response = requests.delete(url=f'https://reqres.in/api/users/{user_to_delete}')

    assert response.status_code == 204
