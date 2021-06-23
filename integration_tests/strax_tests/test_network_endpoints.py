import pytest
from nodes import BaseNode
from api.network.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_disconnect(strax_hot_node: BaseNode):
    peer_address = '[::ffff:127.0.0.2]'
    strax_hot_node.network.disconnect(peer_address=peer_address)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_setban(strax_hot_node: BaseNode):
    peer_address = '[::ffff:127.0.0.2]'
    strax_hot_node.network.set_ban(
        ban_command='add',
        ban_duration_seconds=60,
        peer_address=peer_address
    )


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_getbans(strax_hot_node: BaseNode):
    peer_address = '[::ffff:127.0.0.3]'
    strax_hot_node.network.set_ban(
        ban_command='add',
        ban_duration_seconds=60,
        peer_address=peer_address
    )
    response = strax_hot_node.network.get_bans()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, BannedPeerModel)


@pytest.mark.integration_test
@pytest.mark.strax_integration_test
def test_clear_banned(strax_hot_node: BaseNode):
    strax_hot_node.network.clear_banned()
