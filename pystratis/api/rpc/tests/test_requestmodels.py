import json
from pystratis.api.rpc.requestmodels import *


def test_callbynamerequest():
    data = {
        'methodName': 'rpccommand'
    }
    request_model = CallByNameRequest(
        method_name=data['methodName']
    )
    assert json.dumps(data) == request_model.json()
