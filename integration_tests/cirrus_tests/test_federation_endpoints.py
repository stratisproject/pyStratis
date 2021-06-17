import pytest
from nodes import CirrusMinerNode
from api.federation.responsemodels import *


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


@pytest.mark.skip(reason='Endpoint not active for cirrus network with devmode active.')
@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_member(cirrusminer_node: CirrusMinerNode):
    response = cirrusminer_node.federation.members()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, FederationMemberModel)
