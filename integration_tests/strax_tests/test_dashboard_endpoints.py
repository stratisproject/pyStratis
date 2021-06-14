import pytest
from nodes import BaseNode


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_asyncloopsstats(strax_hot_node: BaseNode):
    response = strax_hot_node.dashboard.asyncloops_stats()
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_stats(strax_hot_node: BaseNode):
    response = strax_hot_node.dashboard.stats()
    assert isinstance(response, str)
