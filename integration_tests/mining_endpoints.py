from typing import Union
from nodes import StraxNode, InterfluxStraxNode
from api.mining.requestmodels import *


def check_mining_endpoints(node: Union[StraxNode, InterfluxStraxNode], num_blocks_to_mine: int) -> None:
    assert check_generate(node=node, count=num_blocks_to_mine)
    assert check_stop_mining(node=node)


def check_generate(node: StraxNode, count: int = 1) -> bool:
    node.mining.generate(GenerateRequest(block_count=count))
    return True


def check_stop_mining(node: StraxNode) -> bool:
    node.mining.stop_mining()
    return True
