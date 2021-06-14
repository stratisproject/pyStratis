import pytest
from nodes import StraxNode
from api.mining.requestmodels import *
from api.mining.responsemodels import *
from pybitcoin.types import uint256


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_generate(strax_hot_node: StraxNode):
    response = strax_hot_node.mining.generate(GenerateRequest(block_count=1))
    assert isinstance(response, GenerateBlocksModel)
    assert len(response.blocks) == 1
    for item in response.blocks:
        assert isinstance(item, uint256)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_stop_mining(strax_hot_node: StraxNode):
    # Works, but interferes with other tests by killing and disposing of the miner.
    pass
