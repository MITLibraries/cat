import pytest

import cat


@pytest.fixture
def client():
    cat.app.config['TESTING'] = True
    with cat.app.test_client() as client:
        yield client


def test_cat_is_cat(client):
    r = client.get('/')
    assert '🐱' in r.data.decode('utf-8')
