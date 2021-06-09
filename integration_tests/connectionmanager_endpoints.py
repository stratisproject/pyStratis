import time
from nodes import BaseNode


def get_node_endpoint(node: BaseNode) -> str:
    localhost_ip = node.ipaddr.replace('http://localhost', '[::ffff:127.0.0.1]')
    return f'{localhost_ip}:{node.blockchainnetwork.DEFAULT_PORT}'


def check_connection_manager_endpoints(a: BaseNode, b: BaseNode) -> None:
    assert check_add_node(a, b)
    assert check_peerinfo(a, b)


def check_add_node(a: BaseNode, b: BaseNode) -> bool:
    from api.connectionmanager.requestmodels import AddNodeRequest
    request_model = AddNodeRequest(endpoint=get_node_endpoint(b), command='add')
    a.connection_manager.addnode(request_model)
    # Wait for handshake
    time.sleep(5)
    return True


def check_peerinfo(a: BaseNode, b: BaseNode) -> bool:
    peerinfo = a.connection_manager.getpeerinfo()
    assert len(peerinfo) == 1
    assert peerinfo[0].addr == get_node_endpoint(b)
    return True
