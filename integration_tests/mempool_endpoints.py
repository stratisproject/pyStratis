from nodes import BaseNode


def check_mempool_endpoints(node: BaseNode):
    assert check_raw_mempool(node)


def check_raw_mempool(node: BaseNode) -> bool:
    node.mempool.get_raw_mempool()
    return True
