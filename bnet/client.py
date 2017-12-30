from bnet.exceptions import IncorrectMethod


class BattleNetClient(object):

    def __init__(self, connection):
        self.connection = connection

        self._method = None
        self._endpoint = None

    def __getattr__(self, endpoint):
        if '_' in endpoint:
            endpoint = endpoint.split('_')
            self._endpoint = '/'.join(endpoint[1:])
            self._method = endpoint[0].upper()

        else:
            raise IncorrectMethod(endpoint)

        return self

    def __call__(self, *args, **kwargs):
        endpoint_arguments = '/'.join(args)
        return self.connection._make_request(
            method=self._method,
            endpoint=self._endpoint,
            endpoint_arguments=endpoint_arguments,
            parameters=kwargs
        )
