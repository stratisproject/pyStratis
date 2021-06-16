import pytest
from nodes import CirrusMinerNode, CirrusNode
from api.consensus.requestmodels import *
from api.consensus.responsemodels import *
from pybitcoin.types import uint256


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_deployment_flags(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode, wait_x_blocks_and_sync):
    wait_x_blocks_and_sync(1)
    response = cirrusminer_node.consensus.deployment_flags()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, DeploymentFlagsModel)

    response = cirrus_syncing_node.consensus.deployment_flags()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, DeploymentFlagsModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_best_block_hash(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode, wait_x_blocks_and_sync):
    wait_x_blocks_and_sync(1)
    response = cirrusminer_node.consensus.get_best_blockhash()
    assert isinstance(response, uint256)

    response = cirrus_syncing_node.consensus.get_best_blockhash()
    assert isinstance(response, uint256)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_block_hash(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode, wait_x_blocks_and_sync):
    wait_x_blocks_and_sync(1)
    request_model = GetBlockHashRequest(height=1)
    response = cirrusminer_node.consensus.get_blockhash(request_model)
    assert isinstance(response, uint256)

    request_model = GetBlockHashRequest(height=1)
    response = cirrus_syncing_node.consensus.get_blockhash(request_model)
    assert isinstance(response, uint256)
