import requests
import pytest

URL = "https://api.openbrewerydb.org/"


def test_get_all_brewery():
    response = requests.get(f'{URL}breweries')
    assert response.status_code == 200


@pytest.mark.parametrize('count, status_code', [(0, 200), (-1, 500)])
def test_random_brewery_size(count, status_code):
    result = requests.get(f'{URL}breweries/random?size={count}')
    assert result.status_code == status_code


@pytest.mark.parametrize('city', ["Knox", "Bend", "Denver"])
def test_random_brewery_by_city(city):
    result = requests.get(f'{URL}breweries?by_city={city}')
    assert result.status_code == 200
    assert result.json()[0]["city"] == city


@pytest.mark.parametrize('postal_code', ["46534", "97701-9847", "97703-2465"])
def test_random_brewery_by_postal(postal_code):
    result = requests.get(f'{URL}breweries?by_postal={postal_code}')
    assert result.status_code == 200
    assert result.json()[0]["postal_code"] == postal_code


@pytest.mark.parametrize('search', ["Dog", "cat"])
def test_brewery_search(search):
    result = requests.get(f'{URL}breweries/autocomplete?query={search}')
    assert result.status_code == 200
