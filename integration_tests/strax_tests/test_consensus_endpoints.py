import pytest
from pystratis.nodes import BaseNode
from pystratis.core.types import uint256
from pystratis.api.consensus.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_deployment_flags(strax_hot_node: BaseNode):
    response = strax_hot_node.consensus.deployment_flags()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, DeploymentFlagsModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_best_block_hash(strax_hot_node: BaseNode):
    response = strax_hot_node.consensus.get_best_blockhash()
    assert isinstance(response, uint256)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_get_block_hash(strax_hot_node: BaseNode):
    response = strax_hot_node.consensus.get_blockhash(height=1)
    assert isinstance(response, uint256)
