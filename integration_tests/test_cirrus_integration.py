import pytest
import api
from git_checkout_current_node_version import git_checkout_current_node_version


@pytest.mark.skip
def test_cirrus_integration(cirrus_start_regtest_node, stop_regtest_node):
    git_checkout_current_node_version(api.__version__)
    test_node = cirrus_start_regtest_node(port=12345)
    # TODO
    test_node.check_all_endpoints_implemented()
    stop_regtest_node(test_node)
