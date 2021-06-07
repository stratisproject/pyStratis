import pytest
from pytest_mock import MockerFixture
from api.smartcontracts import SmartContracts


@pytest.mark.skip
def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if SmartContracts.route + '/' in endpoint:
            assert endpoint in SmartContracts.endpoints


@pytest.mark.skip
def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if SmartContracts.route + '/' in endpoint:
            assert endpoint in SmartContracts.endpoints


@pytest.mark.skip
def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if SmartContracts.route + '/' in endpoint:
            assert endpoint in SmartContracts.endpoints


@pytest.mark.skip
def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if SmartContracts.route + '/' in endpoint:
            assert endpoint in SmartContracts.endpoints

# @pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])


def test_code():
    # TODO
    pass

def test_balance():
    # TODO
    pass

def test_storage():
    # TODO
    pass

def test_receipt():
    # TODO
    pass

def test_receipt_search():
    # TODO
    pass

def test_build_create():
    # TODO
    pass

def test_build_call():
    # TODO
    pass

def test_build_transaction():
    # TODO
    pass

def test_estimate_fee():
    # TODO
    pass

def test_build_and_send_create():
    # TODO
    pass

def test_build_and_send_call():
    # TODO
    pass

def test_local_call():
    # TODO
    pass

def test_address_balances():
    # TODO
    pass


