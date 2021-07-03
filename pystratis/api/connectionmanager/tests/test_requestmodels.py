import pytest
import json
from pystratis.api.connectionmanager.requestmodels import *


def test_addnoderequest_bad_command_raises_valueerror():
    with pytest.raises(ValueError):
        AddNodeRequest(
            endpoint='http://localhost',
            command='badcommand'
        )


def test_addnoderequest():
    data = {
        'endpoint': 'http://localhost',
        'command': 'add'
    }
    request_model = AddNodeRequest(
        endpoint='http://localhost',
        command='add'
    )
    assert json.dumps(data) == request_model.json()
