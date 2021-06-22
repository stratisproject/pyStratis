import pytest
from api.federationgateway.requestmodels import *
from api.federationgateway.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_deposits(interflux_cirrusminer_node):
    request_model = DepositsRequest(block_height=5)
    response = interflux_cirrusminer_node.federation_gateway.deposits(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, MaturedBlockDepositsModel)


@pytest.mark.skip(reason='WIP')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_pending_transfer(interflux_cirrusminer_node):
    request_model = PendingTransferRequest(
        deposit_id=data[0]['depositId'],
        transaction_id=txid
    )

    response = interflux_cirrusminer_node.federation_gateway.pending_transfer(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, CrossChainTransferModel)


@pytest.mark.skip(reason='WIP')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_fullysigned_transfer(interflux_cirrusminer_node):
    request_model = FullySignedTransferRequest(
        deposit_id=data[0]['depositId'],
        transaction_id=txid
    )
    response = interflux_cirrusminer_node.federation_gateway.fullysigned_transfer(request_model)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, CrossChainTransferModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_member_info(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.federation_gateway.member_info()
    assert isinstance(response, FederationMemberInfoModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_info(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.federation_gateway.info()
    assert isinstance(response, FederationGatewayInfoModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_ip_add(interflux_cirrusminer_node):
    request_model = MemberIPAddRequest(endpoint='http://localhost')
    response = interflux_cirrusminer_node.federation_gateway.ip_add(request_model)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_ip_remove(interflux_cirrusminer_node):
    request_model = MemberIPRemoveRequest(endpoint='http://localhost')
    response = interflux_cirrusminer_node.federation_gateway.ip_remove(request_model)
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_ip_replace(interflux_cirrusminer_node):
    request_model = MemberIPReplaceRequest(
        endpointtouse='http://newhost',
        endpoint='http://localhost'
    )
    response = interflux_cirrusminer_node.federation_gateway.ip_replace(request_model)
    assert isinstance(response, str)


@pytest.mark.skip(reason='WIP')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_verify_transfer(interflux_cirrusminer_node):
    request_model = VerifyTransferRequest(deposit_id_transaction_id=generate_uint256)
    response = interflux_cirrusminer_node.federation_gateway.verify_transfer(request_model)
    assert isinstance(response, ValidateTransactionResultModel)
