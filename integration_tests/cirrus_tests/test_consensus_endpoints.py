import pytest
from nodes import CirrusMinerNode
from api.consensus.responsemodels import *
from pybitcoin.types import uint256


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_deployment_flags(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.consensus.deployment_flags()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, DeploymentFlagsModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_best_block_hash(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.consensus.get_best_blockhash()
    assert isinstance(response, uint256)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_get_block_hash(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.consensus.get_blockhash(height=1)
    assert isinstance(response, uint256)
