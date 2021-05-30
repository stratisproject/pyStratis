import os
import shutil
import subprocess
import pytest
import api
from pybitcoin.networks import StraxRegTest, CirrusRegTest
from nodes import InterfluxStraxNode, InterfluxCirrusNode
from git_checkout_current_node_version import git_checkout_current_node_version


def interflux_start_strax_regtest_node(port: int) -> InterfluxStraxNode:
    """

    Args:
        port:

    Returns:

    """
    source_dir = os.path.join(os.getcwd(), 'StratisFullNode', 'src', 'Stratis.CirrusPegD')
    data_dir = os.path.join(os.getcwd(), 'data_dir', f'interflux-strax-node-{port}')
    shutil.rmtree(data_dir)
    root_dir = os.getcwd()
    baseuri = 'http://localhost'
    node = InterfluxStraxNode(ipaddr=baseuri, blockchainnetwork=StraxRegTest())
    os.chdir(source_dir)
    # TODO fix startup options
    subprocess.Popen(['dotnet', 'run', '-regtest', f'-datadir={data_dir}', '-addressindex=1', f'-apiport={port}', f'-port={port+1}', f'-signalrport={port+2}'])

    os.chdir(root_dir)
    return node


def interflux_stop_strax_regtest_node(node: InterfluxStraxNode):
    pass


def interflux_start_cirrus_regtest_node(port: int) -> InterfluxCirrusNode:
    """

    Args:
        port:

    Returns:

    """
    source_dir = os.path.join(os.getcwd(), 'StratisFullNode', 'src', 'Stratis.CirrusPegD')
    data_dir = os.path.join(os.getcwd(), 'data_dir', f'interflux-cirrus-node-{port}')
    shutil.rmtree(data_dir)
    root_dir = os.getcwd()
    baseuri = 'http://localhost'
    node = InterfluxCirrusNode(ipaddr=baseuri, blockchainnetwork=CirrusRegTest())
    os.chdir(source_dir)
    # TODO fix start options
    subprocess.Popen(['dotnet', 'run', '-regtest', f'-datadir={data_dir}', '-addressindex=1', f'-apiport={port}', f'-port={port+1}', f'-signalrport={port+2}'])

    os.chdir(root_dir)
    return node


def interflux_stop_cirrus_regtest_node(node: InterfluxCirrusNode):
    pass


@pytest.mark.skip
def test_interflux_integration():
    git_checkout_current_node_version(api.__version__)
    strax_node = interflux_start_strax_regtest_node(port=12345)
    cirrus_node = interflux_start_cirrus_regtest_node(port=56789)
    # TODO
    interflux_stop_strax_regtest_node(node=strax_node)
    interflux_stop_cirrus_regtest_node(node=cirrus_node)
