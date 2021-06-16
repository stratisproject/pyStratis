import pytest
from nodes import CirrusMinerNode
from api.consensus.requestmodels import GetBlockHashRequest
from api.notifications.requestmodels import *


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_sync(cirrusminer_node: CirrusMinerNode):
    block_hash = cirrusminer_node.consensus.get_blockhash(GetBlockHashRequest(height=1))
    request_model = SyncRequest(sync_from=block_hash)

    cirrusminer_node.notifications.sync(request_model)
