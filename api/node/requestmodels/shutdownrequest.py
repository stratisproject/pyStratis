import json
from pybitcoin import Model


class ShutdownRequest(Model):
    """A ShutdownRequest."""
    def json(self, *args, **kwargs):
        return json.dumps(True)
