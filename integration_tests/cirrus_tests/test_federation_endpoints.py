import pytest
from nodes import CirrusNode, CirrusMinerNode
from api.federation.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_reconstruct(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    response = cirrusminer_node.federation.reconstruct()
    assert isinstance(response, str)

    response = cirrus_syncing_node.federation.reconstruct()
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_members_current(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    response = cirrusminer_node.federation.members_current()
    assert isinstance(response, FederationMemberDetailedModel)

    response = cirrus_syncing_node.federation.members_current()
    assert not isinstance(response, FederationMemberDetailedModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_member(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    response = cirrusminer_node.federation.members()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, FederationMemberModel)

    response = cirrus_syncing_node.federation.members()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, FederationMemberModel)
