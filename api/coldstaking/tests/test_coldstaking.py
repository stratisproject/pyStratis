import pytest
from pytest_mock import MockerFixture
from api.coldstaking import ColdStaking
from api.coldstaking.requestmodels import *
from api.coldstaking.responsemodels import *
from pybitcoin.networks import StraxMain


def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if ColdStaking.route in endpoint:
            assert endpoint in ColdStaking.endpoints


def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if ColdStaking.route in endpoint:
            assert endpoint in ColdStaking.endpoints


def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if ColdStaking.route in endpoint:
            assert endpoint in ColdStaking.endpoints


def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if ColdStaking.route in endpoint:
            assert endpoint in ColdStaking.endpoints


@pytest.mark.skip
@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_info(mocker: MockerFixture, network, fakeuri):
    # TODO
    request = InfoRequest()
    data = ''
    mocker.patch.object(ColdStaking, 'get', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.info(request_model=request)

    assert response
    assert response
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.skip
@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_account(mocker: MockerFixture, network, fakeuri):
    # TODO
    request = AccountRequest()
    data = ''
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.account(request_model=request)

    assert response
    assert response
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.skip
@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_address(mocker: MockerFixture, network, fakeuri):
    # TODO
    request = AddressRequest()
    data = ''
    mocker.patch.object(ColdStaking, 'get', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.address(request_model=request)

    assert response
    assert response
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.skip
@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_setup_coldstaking(mocker: MockerFixture, network, fakeuri):
    # TODO
    request = SetupRequest()
    data = ''
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.setup(request_model=request)

    assert response
    assert response
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.skip
@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_setup_offline_coldstaking(mocker: MockerFixture, network, fakeuri):
    # TODO
    request = SetupOfflineRequest()
    data = ''
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.setup_offline(request_model=request)

    assert response
    assert response
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.skip
@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_estimate_setup_tx_fee(mocker: MockerFixture, network, fakeuri):
    # TODO
    request = SetupRequest()
    data = ''
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.estimate_setup_tx_fee(request_model=request)

    assert response
    assert response
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.skip
@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_estimate_offline_setup_tx_fee(mocker: MockerFixture, network, fakeuri):
    # TODO
    request = SetupOfflineRequest()
    data = ''
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.estimate_offline_setup_tx_fee(request_model=request)

    assert response
    assert response
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.skip
@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_withdrawal(mocker: MockerFixture, network, fakeuri):
    # TODO
    request = WithdrawalRequest()
    data = ''
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.withdrawal(request_model=request)

    assert response
    assert response
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.skip
@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_offline_withdrawal(mocker: MockerFixture, network, fakeuri):
    # TODO
    request = OfflineWithdrawalRequest()
    data = ''
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.offline_withdrawal(request_model=request)

    assert response
    assert response
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.skip
@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_estimate_offline_withdrawal_fee(mocker: MockerFixture, network, fakeuri):
    # TODO
    request = OfflineWithdrawalFeeEstimationRequest()
    data = ''
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.estimate_offline_withdrawal_tx_fee(request_model=request)

    assert response
    assert response
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()


@pytest.mark.skip
@pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])
def test_coldstaking_estimate_withdrawal_fee(mocker: MockerFixture, network, fakeuri):
    # TODO
    request = WithdrawalRequest()
    data = ''
    mocker.patch.object(ColdStaking, 'post', return_value=data)
    coldstaking = ColdStaking(network=network, baseuri=fakeuri)
    response = coldstaking.estimate_withdrawal_tx_fee(request_model=request)

    assert response
    assert response
    # noinspection PyUnresolvedReferences
    coldstaking.get.assert_called_once()
