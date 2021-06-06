import json
from api.diagnostic.requestmodels import *


def test_getpeerstatisticsrequest():
    data = {
        'connectedOnly': True
    }
    request_model = GetPeerStatisticsRequest(
        connected_only=True
    )
    assert json.dumps(data) == request_model.json()
