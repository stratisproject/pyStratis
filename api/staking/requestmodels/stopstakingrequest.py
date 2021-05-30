import json
from pybitcoin import Model


class StopStakingRequest(Model):
    """A StopStakingRequest."""
    def json(self, *args, **kwargs):
        return json.dumps(True)
