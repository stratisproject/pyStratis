import pytest
from nodes import BaseNode


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_asyncloopsstats(cirrus_hot_node: BaseNode):
    response = cirrus_hot_node.dashboard.asyncloops_stats()
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_stats(cirrus_hot_node: BaseNode):
    response = cirrus_hot_node.dashboard.stats()
    assert isinstance(response, str)
