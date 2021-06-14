import pytest
from nodes import BaseNode
from api.network.requestmodels import *
from api.network.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_disconnect(hot_node: BaseNode):
    peer_address = '[::ffff:127.0.0.2]'
    request_model = DisconnectPeerRequest(peer_address=peer_address)
    hot_node.network.disconnect(request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_setban(hot_node: BaseNode):
    peer_address = '[::ffff:127.0.0.2]'
    request_model = SetBanRequest(
        ban_command='add',
        ban_duration_seconds=60,
        peer_address=peer_address
    )
    hot_node.network.set_ban(request_model)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_getbans(hot_node: BaseNode):
    peer_address = '[::ffff:127.0.0.3]'
    request_model = SetBanRequest(
        ban_command='add',
        ban_duration_seconds=60,
        peer_address=peer_address
    )
    hot_node.network.set_ban(request_model)
    response = hot_node.network.get_bans()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, BannedPeerModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_clear_banned(hot_node: BaseNode):
    request_model = ClearBannedRequest()
    hot_node.network.clear_banned(request_model)
