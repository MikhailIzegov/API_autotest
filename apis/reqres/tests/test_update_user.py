import jsonschema
import requests
import datetime

from apis.reqres.utils.read_json import load_schema


def test_put_user():
    response = requests.put(url='https://reqres.in/api/users/3', json={
            "name": "morpheus555",
            "job": "zion resident"
    })

    schema = load_schema('put_users.json')
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema)


def test_put_user_datetime():
    today_utc = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M')
    response = requests.put(
        url='https://reqres.in/api/users/3',
        json={'name': 'student_name_1', 'job': 'job_name'}
    )

    assert response.status_code == 200
    assert response.json()['updatedAt'][:-8] == today_utc  # Проверка с текущим временем до минуты
