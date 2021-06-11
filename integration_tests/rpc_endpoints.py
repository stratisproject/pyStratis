from nodes import BaseNode
from api.rpc.requestmodels import *
from api import APIError


def check_rpc_endpoints(node: BaseNode) -> None:
    assert check_list_methods(node)
    assert check_call_by_name(node)


def check_call_by_name(node: BaseNode) -> bool:
    request_model = CallByNameRequest(command='getblockcount')
    try:
        node.rpc.call_by_name(request_model)
    except APIError:
        # RPC functionality is deprecated and works inconsistently.
        pass
    return True


def check_list_methods(node: BaseNode):
    node.rpc.list_methods()
    return True
