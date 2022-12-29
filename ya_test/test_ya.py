import requests
import pytest


@pytest.fixture
def default_url():
    return 'https://ya.ru'


@pytest.fixture
def default_status_code():
    return 200


def test_ya(default_url, default_status_code):
    assert requests.get(default_url).status_code == default_status_code
