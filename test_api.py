import requests


def test_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100
