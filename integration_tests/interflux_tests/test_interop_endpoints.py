import pytest
from pystratis.api.interop.responsemodels import *
from pystratis.core import PubKey, DestinationChain
from pystratis.core.types import uint256, hexstr, Money
from pystratis.core.networks import CirrusMain, StraxMain


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_status_burns(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.status_burns()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, ConversionRequestModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_status_mints(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.status_mints()
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, ConversionRequestModel)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_status_votes(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.status_votes()
    assert isinstance(response, dict)
    for item in response:
        assert isinstance(item, Pubkey)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_owners(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.owners(destination_chain=DestinationChain.ETH)
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, str)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_addowner(interflux_cirrusminer_node, generate_p2pkh_address):
    response = interflux_cirrusminer_node.interop.add_owner(
        destination_chain=DestinationChain.ETH,
        new_owner_address=generate_p2pkh_address(network=CirrusMain()),
        gas_price=100
    )
    assert isinstance(response, uint256)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_removeowner(interflux_cirrusminer_node, generate_p2pkh_address):
    response = interflux_cirrusminer_node.interop.remove_owner(
        destination_chain=DestinationChain.ETH,
        existing_owner_address=generate_p2pkh_address(network=CirrusMain()),
        gas_price=100
    )
    assert isinstance(response, uint256)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_confirmtransaction(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.confirm_transaction(
        destination_chain=DestinationChain.ETH,
        transaction_id=1,
        gas_price=100
    )
    assert isinstance(response, uint256)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_changerequirement(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.change_requirement(
        destination_chain=DestinationChain.ETH,
        requirement=1,
        gas_price=100
    )
    assert isinstance(response, uint256)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_multisigtransaction(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.multisig_transaction(
        destination_chain=DestinationChain.ETH,
        transaction_id=1,
        raw=False
    )
    assert isinstance(response, TransactionResponseModel)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_multisigtransaction(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.multisig_transaction(
        destination_chain=DestinationChain.ETH,
        transaction_id=1,
        raw=True
    )
    assert isinstance(response, hexstr)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_multisigconfirmations(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.multisig_confirmations(
        destination_chain=DestinationChain.ETH,
        transaction_id=1
    )
    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, str)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_balance(interflux_cirrusminer_node, generate_p2pkh_address):
    response = interflux_cirrusminer_node.interop.balance(
        destination_chain=DestinationChain.ETH,
        account=generate_p2pkh_address(network=StraxMain())
    )
    assert isinstance(response, Money)


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_requests_delete(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.requests_delete()
    assert isinstance(response, str)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_requests_setoriginator(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.requests_setoriginator(
        request_id=1
    )
    assert isinstance(response, str)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_requests_setnotoriginator(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.requests_setnotoriginator(
        request_id=1
    )
    assert isinstance(response, str)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_requests_reprocess_burn(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.requests_reprocess_burn(
        request_id=1,
        height=1
    )
    assert isinstance(response, str)


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_requests_pushvote(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.requests_pushvote(
        request_id=1,
        vote_id=1
    )
    assert isinstance(response, str)
