import pytest
from nodes import CirrusNode, CirrusMinerNode


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_asyncloopsstats(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    response = cirrusminer_node.dashboard.asyncloops_stats()
    assert isinstance(response, str)

    response = cirrus_syncing_node.dashboard.asyncloops_stats()
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_stats(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    response = cirrusminer_node.dashboard.stats()
    assert isinstance(response, str)

    response = cirrus_syncing_node.dashboard.stats()
    assert isinstance(response, str)
