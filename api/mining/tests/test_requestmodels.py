import json
from api.mining.requestmodels import *


def test_generaterequest():
    data = {
        'blockCount': 5
    }
    request_model = GenerateRequest(
        block_count=5
    )
    assert json.dumps(data) == request_model.json()


def test_stopminingrequest():
    data = True
    request_model = StopMiningRequest(
    )
    assert json.dumps(data) == request_model.json()
