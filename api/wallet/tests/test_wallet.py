import pytest
from pytest_mock import MockerFixture
from api.wallet import Wallet


@pytest.mark.skip
def test_all_strax_endpoints_implemented(strax_swagger_json):
    paths = [key.lower() for key in strax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Wallet.route + '/' in endpoint:
            assert endpoint in Wallet.endpoints


@pytest.mark.skip
def test_all_cirrus_endpoints_implemented(cirrus_swagger_json):
    paths = [key.lower() for key in cirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Wallet.route + '/' in endpoint:
            assert endpoint in Wallet.endpoints


@pytest.mark.skip
def test_all_interfluxstrax_endpoints_implemented(interfluxstrax_swagger_json):
    paths = [key.lower() for key in interfluxstrax_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Wallet.route + '/' in endpoint:
            assert endpoint in Wallet.endpoints


@pytest.mark.skip
def test_all_interfluxcirrus_endpoints_implemented(interfluxcirrus_swagger_json):
    paths = [key.lower() for key in interfluxcirrus_swagger_json['paths'].keys()]
    for endpoint in paths:
        if Wallet.route + '/' in endpoint:
            assert endpoint in Wallet.endpoints

# @pytest.mark.parametrize('network', [StraxMain()], ids=['StraxMain'])


def test_mnemnoic():
    # TODO
    pass

def test_create():
    # TODO
    pass

def test_sign_message():
    # TODO
    pass

def test_pubkey():
    # TODO
    pass

def test_verify_message():
    # TODO
    pass

def test_load():
    # TODO
    pass

def test_recover():
    # TODO
    pass

def test_recover_via_extpubkey():
    # TODO
    pass

def test_general_info():
    # TODO
    pass

def test_transaction_count():
    # TODO
    pass

def test_history():
    # TODO
    pass

def test_balance():
    # TODO
    pass

def test_received_by_address():
    # TODO
    pass

def test_max_balance():
    # TODO
    pass

def test_spendable_transactions():
    # TODO
    pass

def test_estimate_txfee():
    # TODO
    pass

def test_build_transaction():
    # TODO
    pass

def test_build_interflux_transaction():
    # TODO
    pass

def test_send_transaction():
    # TODO
    pass

def test_list_wallets():
    # TODO
    pass

def test_account():
    # TODO
    pass

def test_accounts():
    # TODO
    pass

def test_unused_address():
    # TODO
    pass

def test_unused_addresses():
    # TODO
    pass

def test_new_addresses():
    # TODO
    pass

def test_addresses():
    # TODO
    pass

def test_remove_transactions():
    # TODO
    pass

def test_remove_wallet():
    # TODO
    pass

def test_extpubkey():
    # TODO
    pass

def test_private_key():
    # TODO
    pass

def test_sync():
    # TODO
    pass

def test_sync_from_date():
    # TODO
    pass

def test_wallet_stats():
    # TODO
    pass

def test_split_coins():
    # TODO
    pass

def test_distribute_utxos():
    # TODO
    pass

def test_sweep():
    # TODO
    pass

def test_build_offline_sign_request():
    # TODO
    pass

def test_offline_sign_request():
    # TODO
    pass

def test_consolidate():
    # TODO
    pass

