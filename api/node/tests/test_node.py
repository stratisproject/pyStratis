import pytest
from pytest_mock import MockerFixture
from api.node import Node


@pytest.mark.skip
def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Node.route + '/' in endpoint:
            assert endpoint in Node.endpoints


@pytest.mark.skip
def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Node.route + '/' in endpoint:
            assert endpoint in Node.endpoints


@pytest.mark.skip
def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Node.route + '/' in endpoint:
            assert endpoint in Node.endpoints


@pytest.mark.skip
def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Node.route + '/' in endpoint:
            assert endpoint in Node.endpoints

# @pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])


def test_status():
    # TODO
    pass

def test_get_blockheader():
    # TODO
    pass

def test_get_raw_transaction():
    # TODO
    pass

def test_decode_raw_transaction():
    # TODO
    pass

def test_validate_address():
    # TODO
    pass

def test_get_txout():
    # TODO
    pass

def test_get_txout_proof():
    # TODO
    pass

def test_shutdown():
    # TODO
    pass

def test_stop():
    # TODO
    pass

def test_log_levels():
    # TODO
    pass

def test_log_rules():
    # TODO
    pass

def test_async_loops():
    # TODO
    pass

