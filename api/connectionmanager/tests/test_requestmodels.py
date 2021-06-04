import pytest
from api.connectionmanager.requestmodels import *


def test_addnode_bad_command_raises_valueerror():
    with pytest.raises(ValueError):
        AddNodeRequest(
            endpoint='http://localhost',
            command='badcommand'
        )