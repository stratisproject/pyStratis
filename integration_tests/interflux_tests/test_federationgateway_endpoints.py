import pytest
from api.federationgateway.requestmodels import *
from api.federationgateway.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_deposits(interflux_strax_node):
    request_model = DepositsRequest(block_height=5)
    response = interflux_strax_node.federation_gateway.deposits(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, MaturedBlockDepositsModel)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_pending_transfer(interflux_strax_node):
    request_model = PendingTransferRequest()

    response = interflux_strax_node.federation_gateway.pending_transfer(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, CrossChainTransferModel)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_fullysigned_transfer(interflux_strax_node):
    request_model = FullySignedTransferRequest()
    response = interflux_strax_node.federation_gateway.fullysigned_transfer(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, CrossChainTransferModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_member_info(interflux_strax_node):
    response = interflux_strax_node.federation_gateway.member_info()
    assert isinstance(response, FederationMemberInfoModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_info(interflux_strax_node):
    response = interflux_strax_node.federation_gateway.info()
    assert isinstance(response, FederationGatewayInfoModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_ip_add(interflux_strax_node):
    request_model = MemberIPAddRequest(endpoint='127.0.0.1')
    response = interflux_strax_node.federation_gateway.ip_add(request_model)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_ip_remove(interflux_strax_node):
    request_model = MemberIPRemoveRequest(endpoint='127.0.0.1')
    response = interflux_strax_node.federation_gateway.ip_remove(request_model)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_ip_replace(interflux_strax_node):
    request_model = MemberIPReplaceRequest(
        endpointtouse='127.0.0.2',
        endpoint='127.0.0.1'
    )
    response = interflux_strax_node.federation_gateway.ip_replace(request_model)
    assert isinstance(response, str)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_verify_transfer(interflux_strax_node, generate_uint256):
    request_model = VerifyTransferRequest(deposit_id_transaction_id=generate_uint256)
    response = interflux_strax_node.federation_gateway.verify_transfer(request_model)
    assert isinstance(response, ValidateTransactionResultModel)
