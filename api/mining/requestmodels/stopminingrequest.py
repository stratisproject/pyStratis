import json
from pybitcoin import Model


class StopMiningRequest(Model):
    """A StopMiningRequest."""
    def json(self, *args, **kwargs):
        return json.dumps(True)
