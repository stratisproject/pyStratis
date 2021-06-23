import pytest
from api.federationgateway.requestmodels import *
from api.federationgateway.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_deposits(interflux_strax_node):
    response = interflux_strax_node.federation_gateway.deposits(block_height=5)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, MaturedBlockDepositsModel)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_pending_transfer(interflux_strax_node):
    response = interflux_strax_node.federation_gateway.pending_transfer()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, CrossChainTransferModel)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_fullysigned_transfer(interflux_strax_node):
    response = interflux_strax_node.federation_gateway.fullysigned_transfer()
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
    response = interflux_strax_node.federation_gateway.ip_add(endpoint='127.0.0.1')
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_ip_remove(interflux_strax_node):
    response = interflux_strax_node.federation_gateway.ip_remove(endpoint='127.0.0.1')
    assert isinstance(response, str)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_ip_replace(interflux_strax_node):
    response = interflux_strax_node.federation_gateway.ip_replace(
        endpointtouse='127.0.0.2',
        endpoint='127.0.0.1'
    )
    assert isinstance(response, str)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_verify_transfer(interflux_strax_node, generate_uint256):
    response = interflux_strax_node.federation_gateway.verify_transfer(deposit_id_transaction_id=generate_uint256)
    assert isinstance(response, ValidateTransactionResultModel)
