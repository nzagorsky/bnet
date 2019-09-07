import os
import requests

from bnet.exceptions import BattleNetError

AUTH_URL = "https://us.battle.net/oauth/token"


def generate_access_token(client_id=None, secret=None):
    if not all([client_id, secret]):
        try:
            client_id = os.environ["BATTLE_NET_CLIENT_ID"]
            secret = os.environ["BATTLE_NET_SECRET"]
        except KeyError:
            raise ValueError(
                "Either provide client_id and secret or set environment variables BATTLE_NET_CLIENT_ID, BATTLE_NET_SECRET"
            )

    response = requests.post(
        AUTH_URL, auth=(client_id, secret), data={"grant_type": "client_credentials"}
    ).json()
    if "error" in response:
        raise BattleNetError(response)
    else:
        return response
