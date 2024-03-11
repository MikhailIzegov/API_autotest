import os

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope='module', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='module', autouse=False)
def login():
    return os.getenv('LOGIN')


@pytest.fixture(scope='module', autouse=False)
def password():
    return os.getenv('PASSWORD')
