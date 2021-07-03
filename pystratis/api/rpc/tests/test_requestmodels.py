import json
from pystratis.api.rpc.requestmodels import *


def test_callbynamerequest():
    data = {
        'command': 'rpccommand'
    }
    request_model = CallByNameRequest(
        command=data['command']
    )
    assert json.dumps(data) == request_model.json()
