import pytest
from pystratis.nodes import CirrusMinerNode, CirrusNode
from pystratis.api.federation.responsemodels import *
from pystratis.core import PubKey


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_reconstruct(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.federation.reconstruct()
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_members_current(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.federation.members_current()
    assert isinstance(response, FederationMemberDetailedModel)


@pytest.mark.xfail
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_member(cirrus_node: CirrusNode):
    response = cirrus_node.federation.members()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, FederationMemberModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_miner_at_height(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.federation.miner_at_height(block_height=1)
    assert isinstance(response, PubKey)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_federation_at_height(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.federation.federation_at_height(block_height=1)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, PubKey)
