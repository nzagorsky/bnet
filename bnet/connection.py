import logging
import os
import urllib

import requests

from bnet.client import BattleNetClient
from bnet.exceptions import BattleNetError

LOG = logging.getLogger('battle.net')

BASE_URL = 'https://{region}.api.battle.net/{game}/{endpoint}/{endpoint_arguments}?{parameters}'


class BattleNetConnection(object):
    def __init__(self, apikey='', locale='en_GB', region='eu', game='wow'):
        """
        Connection class for Battle.net API client.

        :param str apikey: If None is passed env key is used.
        :param str game:
        :param str locale:
        :param str region:
        """
        apikey = apikey or os.environ.get('BATTLE_NET_APIKEY', '')
        if not apikey:
            LOG.critical('No Battle.net API key provided')
            raise ValueError('Set BATTLE_NET_APIKEY env variable or pass '
                             'apikey as a parameter')

        self.apikey = apikey
        self.locale = locale
        self.game = game
        self.region = region

        self.session = requests.Session()

    def _build_url(self, parameters, endpoint, endpoint_arguments, **kwargs):
        """
        Endpoint arguments is passed as arguments to `BattleNetClient` methods.
        """
        if isinstance(parameters, dict):
            parameters.update({'apikey': self.apikey, 'locale': self.locale})
            formatted_parameters = urllib.parse.urlencode(parameters)

        else:
            raise TypeError('Invalid parameters passed. Should be dict.')

        url = BASE_URL.format(
            region=self.region,
            game=self.game,
            endpoint=endpoint,
            endpoint_arguments=endpoint_arguments,
            parameters=formatted_parameters,
        )
        LOG.debug('URL: {}'.format(url))
        return url

    def _make_request(self, method, endpoint, endpoint_arguments, parameters,
                      **kwargs):

        url = self._build_url(parameters, endpoint, endpoint_arguments,
                              **kwargs)
        LOG.debug('Fetching')
        response = self.session.request(method, url)
        LOG.debug('Got response {}'.format(response.status_code))

        if not 199 < response.status_code < 300:
            raise BattleNetError(response.json())

        return response.json()

    def client(self, *args, **kwargs):
        return BattleNetClient(connection=self)
