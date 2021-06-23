import pytest
from nodes import CirrusMinerNode
from api.network.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_disconnect(cirrusminer_node: CirrusMinerNode):
    peer_address = '[::ffff:127.0.0.2]'
    cirrusminer_node.network.disconnect(peer_address=peer_address)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_setban(cirrusminer_node: CirrusMinerNode):
    peer_address = '[::ffff:127.0.0.2]'
    cirrusminer_node.network.set_ban(
        ban_command='add',
        ban_duration_seconds=60,
        peer_address=peer_address
    )


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_getbans(cirrusminer_node: CirrusMinerNode):
    peer_address = '[::ffff:127.0.0.3]'
    cirrusminer_node.network.set_ban(
        ban_command='add',
        ban_duration_seconds=60,
        peer_address=peer_address
    )
    response = cirrusminer_node.network.get_bans()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, BannedPeerModel)


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_clear_banned(cirrusminer_node: CirrusMinerNode):
    cirrusminer_node.network.clear_banned()
