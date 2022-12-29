import pytest
import requests

URL = 'https://jsonplaceholder.typicode.com'


@pytest.mark.parametrize('resource, status_code', [('posts', 200), ('comments', 200), ('cat', 404)])
def test_get_resource(resource, status_code):
    response = requests.get(f'{URL}/{resource}')
    assert response.status_code == status_code


@pytest.mark.parametrize('id, status_code', [(1, 200), ('string', 404), (0, 404)])
def test_get_post_with_id(id, status_code):
    response = requests.get(f'{URL}/posts/{id}')
    assert response.status_code == status_code


def test_create_post():
    data = {"userId": 1,
            "id": 1,
            "title": "Lorem Ipsum ",
            "body": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
            }
    response = requests.post(f'{URL}/posts', data)
    assert response.status_code == 201


def test_delete_post(id=1):
    response = requests.delete(f'{URL}/posts/{id}')
    assert response.status_code == 200


@pytest.mark.parametrize('user_id', list(range(1, 10)))
def test_all_users(user_id):
    response = requests.get(f'{URL}/users/{user_id}')
    assert response.status_code == 200
