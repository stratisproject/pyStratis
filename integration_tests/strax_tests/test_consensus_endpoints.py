import pytest
from nodes import BaseNode
from api.consensus.requestmodels import *
from api.consensus.responsemodels import *
from pybitcoin.types import uint256


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_deployment_flags(hot_node: BaseNode):
    response = hot_node.consensus.deployment_flags()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, DeploymentFlagsModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_best_block_hash(hot_node: BaseNode):
    response = hot_node.consensus.get_best_blockhash()
    assert isinstance(response, uint256)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_block_hash(hot_node: BaseNode):
    request_model = GetBlockHashRequest(height=1)
    response = hot_node.consensus.get_blockhash(request_model)
    assert isinstance(response, uint256)
