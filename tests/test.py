
import pytest
from pytest import raises

from api.connection import BattleNetConnection
from api.exceptions import BattleNetError


# TODO add mocks for requests lib to avoid bnet servers queries.
@pytest.fixture()
def client():
    conn = BattleNetConnection()
    client = conn.client()
    return client


def test_correct_data(client):
    response = client.get_auction_data('Kazzak')
    assert client._endpoint == 'auction/data'
    assert response['files']


def test_incorrect_path(client):
    with raises(BattleNetError):
        client.get_unknown_stuff()
