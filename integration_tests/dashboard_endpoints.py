from typing import Union
from nodes import StraxNode, CirrusNode


def check_dashboard_endpoints(node: Union[StraxNode, CirrusNode]):
    assert check_asyncloopsstats(node)
    assert check_stats(node)


def check_asyncloopsstats(node: Union[StraxNode, CirrusNode]) -> bool:
    node.dashboard.asyncloops_stats()
    return True


def check_stats(node: Union[StraxNode, CirrusNode]) -> bool:
    node.dashboard.stats()
    return True
