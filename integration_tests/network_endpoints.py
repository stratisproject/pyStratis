from nodes import BaseNode
from api.network.requestmodels import *


def check_network_endpoints(node: BaseNode, peer_address: str):
    assert check_setban(node, peer_address)
    assert check_getbans(node)
    assert check_clear_banned(node)
    assert check_disconnect(node, peer_address)


def check_disconnect(node: BaseNode, peer_address: str) -> bool:
    request_model = DisconnectPeerRequest(peer_address=peer_address)
    node.network.disconnect(request_model)
    return True


def check_setban(node: BaseNode, peer_address: str) -> bool:
    request_model = SetBanRequest(
        ban_command='add',
        ban_duration_seconds=60,
        peer_address=peer_address
    )
    node.network.set_ban(request_model)
    return True


def check_getbans(node: BaseNode):
    node.network.get_bans()
    return True


def check_clear_banned(node: BaseNode):
    request_model = ClearBannedRequest()
    node.network.clear_banned(request_model)
    return True
