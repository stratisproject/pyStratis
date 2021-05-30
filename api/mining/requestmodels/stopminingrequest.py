import json
from pybitcoin import Model


class StopMiningRequest(Model):
    """A StopMiningRequest."""
    def json(self, *args, **kwargs):
        json.dumps(True)
