import os
import shutil
import subprocess
import pytest
import api
from pybitcoin.networks import StraxRegTest
from nodes import StraxNode
from git_checkout_current_node_version import git_checkout_current_node_version


def strax_start_regtest_node(port: int) -> StraxNode:
    source_dir = os.path.join(os.getcwd(), 'StratisFullNode', 'src', 'Stratis.StraxD')
    data_dir = os.path.join(os.getcwd(), 'data_dir', f'strax-node-{port}')
    shutil.rmtree(data_dir)
    root_dir = os.getcwd()
    baseuri = 'http://localhost'
    node = StraxNode(ipaddr=baseuri, blockchainnetwork=StraxRegTest())
    os.chdir(source_dir)
    subprocess.Popen(['dotnet', 'run', '-regtest', f'-datadir={data_dir}', '-addressindex=1', f'-apiport={port}', f'-port={port+1}', f'-signalrport={port+2}'])
    os.chdir(root_dir)
    return node


def strax_stop_regtest_node(node: StraxNode):
    pass


@pytest.mark.skip
def test_strax_integration():
    git_checkout_current_node_version(api.__version__)
    node = strax_start_regtest_node(port=12345)
    # TODO
    strax_stop_regtest_node(node=node)
