import pytest
from pytest import raises

from bnet.connection import BattleNetConnection
from bnet.exceptions import BattleNetError
from bnet.utils import generate_access_token


@pytest.fixture()
def client():
    conn = BattleNetConnection()
    client = conn.client()
    return client


def test_generate_access_token():
    response = generate_access_token()
    assert response["access_token"]


def test_correct_data(client):
    response = client.get_auction_data("Draenor")
    assert client._endpoint == "auction/data"
    assert response["files"]


def test_incorrect_path(client):
    with raises(BattleNetError):
        client.get_unknown_stuff()
