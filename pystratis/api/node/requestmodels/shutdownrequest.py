import json
from pystratis.api import Model


class ShutdownRequest(Model):
    """A request model for the node/shutdown and node/stop endpoints."""
    def json(self, *args, **kwargs):
        return json.dumps(True)
