import json
from pystratis.api.notifications.requestmodels import *


def test_syncrequest(generate_uint256):
    data = {
        'from': generate_uint256
    }
    request_model = SyncRequest(
        sync_from=data['from']
    )
    assert json.dumps(data) == request_model.json()
