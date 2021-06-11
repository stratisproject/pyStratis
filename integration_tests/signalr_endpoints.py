from nodes import BaseNode


def check_signalr_endpoints(node: BaseNode):
    assert check_get_connection_info(node)


def check_get_connection_info(node: BaseNode) -> bool:
    node.signalr.get_connection_info()
    return True
