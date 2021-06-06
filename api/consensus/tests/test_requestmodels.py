import json
from api.consensus.requestmodels import *


def test_getblockhashrequest():
    data = {
        'height': 1
    }
    request_model = GetBlockHashRequest(
        height=1
    )
    assert json.dumps(data) == request_model.json()
