import os
import pytest


@pytest.fixture(scope='module', autouse=False)
def login():
    return os.getenv('LOGIN')


@pytest.fixture(scope='module', autouse=False)
def password():
    return os.getenv('PASSWORD')
