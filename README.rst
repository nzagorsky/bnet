
Battle.net API for Python
=========================


Usage:
------

.. code-block:: python

    from api.connection import BattleNetConnection
    connection = BattleNetConnection(apikey=<BATTLE_NET_APIKEY>)
    client = conn.client()
    client.get_auction_data(server)


Tests:
------

```
make test
```
