import os
import shutil
import subprocess
import pytest
import api
from nodes import CirrusNode
from pybitcoin.networks import CirrusRegTest
from git_checkout_current_node_version import git_checkout_current_node_version


def cirrus_start_regtest_node(port: int) -> CirrusNode:
    """

    Args:
        port:

    Returns:

    """
    source_dir = os.path.join(os.getcwd(), 'StratisFullNode', 'src', 'Stratis.CirrusD')
    data_dir = os.path.join(os.getcwd(), 'data_dir', f'cirrus-node-{port}')
    shutil.rmtree(data_dir)
    root_dir = os.getcwd()
    baseuri = 'http://localhost'
    node = CirrusNode(ipaddr=baseuri, blockchainnetwork=CirrusRegTest())
    os.chdir(source_dir)
    subprocess.Popen(['dotnet', 'run', '-regtest', f'-datadir={data_dir}', '-addressindex=1', f'-apiport={port}', f'-port={port+1}', f'-signalrport={port+2}'])

    os.chdir(root_dir)
    return node


def cirrus_stop_regtest_node(node: CirrusNode) -> None:
    pass


@pytest.mark.skip
def test_cirrus_integration():
    git_checkout_current_node_version(api.__version__)
    node = cirrus_start_regtest_node(port=12345)
    # TODO
    cirrus_stop_regtest_node(node)
