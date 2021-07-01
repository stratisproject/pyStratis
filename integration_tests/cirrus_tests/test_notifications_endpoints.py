import pytest
from nodes import CirrusMinerNode


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_sync(cirrusminer_node: CirrusMinerNode):
    block_hash = cirrusminer_node.consensus.get_blockhash(height=1)
    cirrusminer_node.notifications.sync(sync_from=block_hash)
