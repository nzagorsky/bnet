
Battle.net API for Python
=========================


Usage:
------

.. code-block:: python

    >>> from api.connection import BattleNetConnection
    >>> connection = BattleNetConnection(apikey=<BATTLE_NET_APIKEY>)
    >>> client = conn.client()
    >>> client.get_auction_data(server)
    
    
Documentation:
--------------
https://dev.battle.net/io-docs


Tests:
------

.. code-block:: sh

   $ export BATTLE_NET_APIKEY=<BATTLE_NET_APIKEY>
   $ make test
