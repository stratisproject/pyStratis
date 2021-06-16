import pytest
from nodes import CirrusMinerNode, CirrusNode
from api.network.requestmodels import *
from api.network.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_disconnect(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    peer_address = '[::ffff:127.0.0.2]'
    request_model = DisconnectPeerRequest(peer_address=peer_address)
    cirrusminer_node.network.disconnect(request_model)
    cirrus_syncing_node.network.disconnect(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_setban(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    peer_address = '[::ffff:127.0.0.2]'
    request_model = SetBanRequest(
        ban_command='add',
        ban_duration_seconds=60,
        peer_address=peer_address
    )
    cirrusminer_node.network.set_ban(request_model)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_getbans(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    peer_address = '[::ffff:127.0.0.3]'
    request_model = SetBanRequest(
        ban_command='add',
        ban_duration_seconds=60,
        peer_address=peer_address
    )
    cirrusminer_node.network.set_ban(request_model)
    response = cirrusminer_node.network.get_bans()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, BannedPeerModel)
    cirrus_syncing_node.network.set_ban(request_model)
    response = cirrus_syncing_node.network.get_bans()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, BannedPeerModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_clear_banned(cirrusminer_node: CirrusMinerNode, cirrus_syncing_node: CirrusNode):
    request_model = ClearBannedRequest()
    cirrusminer_node.network.clear_banned(request_model)
    cirrus_syncing_node.network.clear_banned(request_model)
