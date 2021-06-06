import json
from pybitcoin import Model


class ClearBannedRequest(Model):
    """A ClearBannedRequest."""
    def json(self, *args, **kwargs):
        return json.dumps(True)
