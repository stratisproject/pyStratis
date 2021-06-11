from nodes import BaseNode
from api.consensus.requestmodels import *


def check_consensus_endpoints(node: BaseNode, height: int):
    assert check_deployment_flags(node)
    assert check_get_best_block_hash(node)
    assert check_get_block_hash(node, height)


def check_deployment_flags(node: BaseNode) -> bool:
    node.consensus.deployment_flags()
    return True


def check_get_best_block_hash(node: BaseNode):
    node.consensus.get_best_blockhash()
    return True


def check_get_block_hash(node: BaseNode, height: int):
    request_model = GetBlockHashRequest(
        height=height
    )
    node.consensus.get_blockhash(request_model)
    return True
