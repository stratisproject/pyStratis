import json
from pybitcoin import Model


class ClearBannedRequest(Model):
    """A ClearBannedRequest."""
    def json(self, *args, **kwargs):
        json.dumps(True)
