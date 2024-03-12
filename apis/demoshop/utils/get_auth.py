import os
import pytest


@pytest.fixture(scope='session', autouse=False)
def login():
    return os.getenv('DEMOSHOP_LOGIN')


@pytest.fixture(scope='session', autouse=False)
def password():
    return os.getenv('DEMOSHOP_PASSWORD')
