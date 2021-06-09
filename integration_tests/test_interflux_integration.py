import pytest
import api
from git_checkout_current_node_version import git_checkout_current_node_version


@pytest.mark.skip
def test_interflux_integration(interflux_strax_start_regtest_node, interflux_cirrus_start_regtest_node, stop_regtest_node):
    git_checkout_current_node_version(api.__version__)
    strax_test_node = interflux_strax_start_regtest_node(port=12345)
    cirrus_test_node = interflux_cirrus_start_regtest_node(port=56789)
    # TODO
    strax_test_node.check_all_endpoints_implemented()
    cirrus_test_node.check_all_endpoints_implemented()
    stop_regtest_node(strax_test_node)
    stop_regtest_node(cirrus_test_node)
