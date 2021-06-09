import pytest
import os
import shutil
import subprocess
import time
from requests.exceptions import ConnectionError
from nodes import StraxNode, CirrusNode, InterfluxCirrusNode, InterfluxStraxNode, BaseNode
from pybitcoin.networks import StraxRegTest, CirrusRegTest


@pytest.fixture(scope='session')
def strax_start_regtest_node():
    def _strax_start_regtest_node(port: int) -> StraxNode:
        source_dir = os.path.join(os.getcwd(), 'StratisFullNode', 'src', 'Stratis.StraxD')
        data_dir = os.path.join(os.getcwd(), 'data_dir', f'strax-node-{port}')
        if os.path.exists(data_dir):
            shutil.rmtree(data_dir)
        root_dir = os.getcwd()
        baseuri = 'http://localhost'
        node = StraxNode(ipaddr=baseuri, blockchainnetwork=StraxRegTest(
            API_PORT=port,
            DEFAULT_PORT=port+1,
            SIGNALR_PORT=port+2
        ))
        os.chdir(source_dir)
        subprocess.Popen(['dotnet', 'run', '-regtest', f'-datadir={data_dir}', '-addressindex=1', '-server=1', f'-apiport={port}', f'-port={port+1}', f'-signalrport={port+2}'])
        os.chdir(root_dir)
        while True:
            try:
                node.node.status()
                break
            except ConnectionError:
                time.sleep(5)
        print('Node started.')
        return node
    return _strax_start_regtest_node


@pytest.fixture(scope='session')
def cirrus_start_regtest_node():
    def _cirrus_start_regtest_node(port: int) -> CirrusNode:
        source_dir = os.path.join(os.getcwd(), 'StratisFullNode', 'src', 'Stratis.CirrusD')
        data_dir = os.path.join(os.getcwd(), 'data_dir', f'cirrus-node-{port}')
        if os.path.exists(data_dir):
            shutil.rmtree(data_dir)
        root_dir = os.getcwd()
        baseuri = 'http://localhost'
        node = CirrusNode(ipaddr=baseuri, blockchainnetwork=CirrusRegTest(
            API_PORT=port,
            DEFAULT_PORT=port + 1,
            SIGNALR_PORT=port + 2
        ))
        os.chdir(source_dir)
        subprocess.Popen(['dotnet', 'run', '-regtest', f'-datadir={data_dir}', '-addressindex=1', '-server=1' f'-apiport={port}', f'-port={port+1}', f'-signalrport={port+2}'])
        os.chdir(root_dir)
        while True:
            try:
                node.node.status()
                break
            except ConnectionError:
                time.sleep(5)
        print('Node started.')
        return node
    return _cirrus_start_regtest_node


@pytest.fixture(scope='session')
def interflux_strax_start_regtest_node():
    def _interflux_strax_start_regtest_node(port: int) -> InterfluxStraxNode:
        source_dir = os.path.join(os.getcwd(), 'StratisFullNode', 'src', 'Stratis.CirrusPegD')
        data_dir = os.path.join(os.getcwd(), 'data_dir', f'interflux-strax-node-{port}')
        shutil.rmtree(data_dir)
        root_dir = os.getcwd()
        baseuri = 'http://localhost'
        node = InterfluxStraxNode(ipaddr=baseuri, blockchainnetwork=StraxRegTest(
            API_PORT=port,
            DEFAULT_PORT=port + 1,
            SIGNALR_PORT=port + 2
        ))
        os.chdir(source_dir)
        # TODO fix startup options
        subprocess.Popen(['dotnet', 'run', '-regtest', f'-datadir={data_dir}', '-addressindex=1', '-server=1' f'-apiport={port}', f'-port={port+1}', f'-signalrport={port+2}'])
        os.chdir(root_dir)
        while True:
            try:
                node.node.status()
                break
            except ConnectionError:
                time.sleep(5)
        print('Node started.')
        return node
    return _interflux_strax_start_regtest_node


@pytest.fixture(scope='session')
def interflux_cirrus_start_regtest_node():
    def _interflux_cirrus_start_regtest_node(port: int) -> InterfluxCirrusNode:
        source_dir = os.path.join(os.getcwd(), 'StratisFullNode', 'src', 'Stratis.CirrusPegD')
        data_dir = os.path.join(os.getcwd(), 'data_dir', f'interflux-cirrus-node-{port}')
        shutil.rmtree(data_dir)
        root_dir = os.getcwd()
        baseuri = 'http://localhost'
        node = InterfluxCirrusNode(ipaddr=baseuri, blockchainnetwork=CirrusRegTest(
            API_PORT=port,
            DEFAULT_PORT=port + 1,
            SIGNALR_PORT=port + 2
        ))
        os.chdir(source_dir)
        # TODO fix start options
        subprocess.Popen(['dotnet', 'run', '-regtest', f'-datadir={data_dir}', '-addressindex=1', '-server=1' f'-apiport={port}', f'-port={port+1}', f'-signalrport={port+2}'])
        os.chdir(root_dir)
        while True:
            try:
                node.node.status()
                break
            except ConnectionError:
                time.sleep(5)
        print('Node started.')
        return node
    return _interflux_cirrus_start_regtest_node


@pytest.fixture(scope='function')
def stop_regtest_node():
    def _stop_regtest_node(regtest_node: BaseNode) -> None:
        regtest_node.node.stop()
    return _stop_regtest_node
