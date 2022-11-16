import cerberus
import requests
import pytest

URL = "https://dog.ceo/api/"


def test_single_random_image():
    result = requests.get(f'{URL}breeds/image/random')
    schema = {"message": {"type": "string"},
              "status": {"type": "string"}
              }
    valid = cerberus.Validator()
    assert result.status_code == 200
    assert valid.validate(result.json(), schema)


@pytest.mark.parametrize('number, count', [(-1, 1), (0, 1), (49, 49), (51, 50)])
def test_random_image_param(number, count):
    result = requests.get(f'{URL}breeds/image/random/{number}')
    schema = {"message": {"type": "list"},
              "status": {"type": "string"}
              }
    valid = cerberus.Validator()
    assert result.status_code == 200
    assert valid.validate(result.json(), schema)
    assert len(result.json().get('message')) == count


@pytest.mark.parametrize('breed, status_code', [("affenpinscher", 200), ("cat", 404)])
def test_breed_param(breed, status_code):
    result = requests.get(f'{URL}breed/{breed}/images/random/')
    schema = {"code": {"type": "integer"},
              "message": {"type": "string"},
              "status": {"type": "string"}
              }
    valid = cerberus.Validator()
    assert result.status_code == status_code
    assert valid.validate(result.json(), schema)


@pytest.mark.parametrize('breed, count, status_code', [("affenpinscher", 30, 200), ("cat", 22, 404)])
def test_breed_count_param(breed, count, status_code):
    result = requests.get(f'{URL}breed/{breed}/images/random/{count}')
    schema = {"code": {"type": "integer"},
              "message": {"type": ["list", "string"]},
              "status": {"type": "string"}
              }
    valid = cerberus.Validator()
    assert result.status_code == status_code
    assert valid.validate(result.json(), schema)


@pytest.mark.parametrize('breed, status_code', [("affenpinscher", 200), ("cat", 404)])
def test_subbreed_param(breed, status_code):
    result = requests.get(f'{URL}breed/{breed}/list')
    schema = {"message": {"type": ["list", "string"]},
              "status": {"type": "string"},
              "code": {"type": "integer"}
              }
    valid = cerberus.Validator()
    assert result.status_code == status_code
    assert valid.validate(result.json(), schema)
