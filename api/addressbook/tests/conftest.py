import pytest


@pytest.fixture(scope='function')
def addressbookentry_p2pkh(generate_p2pkh_address):
    # noinspection PyUnresolvedReferences
    def _addressbookentry_p2pkh(network: 'BaseNetwork') -> dict:
        return {'address': generate_p2pkh_address(network), 'label': 'TestLabel'}
    return _addressbookentry_p2pkh


@pytest.fixture(scope='function')
def addressbookentry_p2sh(generate_p2sh_address):
    # noinspection PyUnresolvedReferences
    def _addressbookentry_p2sh(network: 'BaseNetwork') -> dict:
        return {'address': generate_p2sh_address(network), 'label': 'TestLabel'}
    return _addressbookentry_p2sh


@pytest.fixture(scope='function')
def addressbookentry_p2wpkh(generate_p2wpkh_address):
    # noinspection PyUnresolvedReferences
    def _addressbookentry_p2wpkh(network: 'BaseNetwork') -> dict:
        return {'address': generate_p2wpkh_address(network), 'label': 'TestLabel'}
    return _addressbookentry_p2wpkh


@pytest.fixture(scope='function')
def addressbookentry_p2wsh(generate_p2wsh_address):
    # noinspection PyUnresolvedReferences
    def _addressbookentry_p2wsh(network: 'BaseNetwork') -> dict:
        return {'address': generate_p2wsh_address(network), 'label': 'TestLabel'}
    return _addressbookentry_p2wsh


@pytest.fixture(scope='function')
def fulladdressbook_p2pkh(generate_p2pkh_address):
    # noinspection PyUnresolvedReferences
    def _fulladdressbook_p2pkh(network: 'BaseNetwork') -> dict:
        return {
            'addresses': [
                {'address': generate_p2pkh_address(network), 'label': 'TestLabel0'},
                {'address': generate_p2pkh_address(network), 'label': 'TestLabel1'},
                {'address': generate_p2pkh_address(network), 'label': 'TestLabel2'},
                {'address': generate_p2pkh_address(network), 'label': 'TestLabel3'},
                {'address': generate_p2pkh_address(network), 'label': 'TestLabel4'},
            ]
        }
    return _fulladdressbook_p2pkh


@pytest.fixture(scope='function')
def fulladdressbook_p2sh(generate_p2sh_address):
    # noinspection PyUnresolvedReferences
    def _fulladdressbook_p2sh(network: 'BaseNetwork') -> dict:
        return {
            'addresses': [
                {'address': generate_p2sh_address(network), 'label': 'TestLabel0'},
                {'address': generate_p2sh_address(network), 'label': 'TestLabel1'},
                {'address': generate_p2sh_address(network), 'label': 'TestLabel2'},
                {'address': generate_p2sh_address(network), 'label': 'TestLabel3'},
                {'address': generate_p2sh_address(network), 'label': 'TestLabel4'},
            ]
        }
    return _fulladdressbook_p2sh


@pytest.fixture(scope='function')
def fulladdressbook_p2wpkh(generate_p2wpkh_address):
    # noinspection PyUnresolvedReferences
    def _fulladdressbook_p2wpkh(network: 'BaseNetwork') -> dict:
        return {
            'addresses': [
                {'address': generate_p2wpkh_address(network), 'label': 'TestLabel0'},
                {'address': generate_p2wpkh_address(network), 'label': 'TestLabel1'},
                {'address': generate_p2wpkh_address(network), 'label': 'TestLabel2'},
                {'address': generate_p2wpkh_address(network), 'label': 'TestLabel3'},
                {'address': generate_p2wpkh_address(network), 'label': 'TestLabel4'},
            ]
        }
    return _fulladdressbook_p2wpkh


@pytest.fixture(scope='function')
def fulladdressbook_p2wsh(generate_p2wsh_address):
    # noinspection PyUnresolvedReferences
    def _fulladdressbook_p2wsh(network: 'BaseNetwork') -> dict:
        return {
            'addresses': [
                {'address': generate_p2wsh_address(network), 'label': 'TestLabel0'},
                {'address': generate_p2wsh_address(network), 'label': 'TestLabel1'},
                {'address': generate_p2wsh_address(network), 'label': 'TestLabel2'},
                {'address': generate_p2wsh_address(network), 'label': 'TestLabel3'},
                {'address': generate_p2wsh_address(network), 'label': 'TestLabel4'},
            ]
        }
    return _fulladdressbook_p2wsh


@pytest.fixture(scope='function')
def partialaddressbook_p2pkh(fulladdressbook_p2pkh):
    # noinspection PyUnresolvedReferences
    def _partialaddressbook_p2pkh(network: 'BaseNetwork') -> dict:
        response = fulladdressbook_p2pkh(network)
        # skip=2, take=2
        return {
            'addresses': response['addresses'][2:4]
        }
    return _partialaddressbook_p2pkh


@pytest.fixture(scope='function')
def partialaddressbook_p2sh(fulladdressbook_p2sh):
    # noinspection PyUnresolvedReferences
    def _partialaddressbook_p2sh(network: 'BaseNetwork') -> dict:
        response = fulladdressbook_p2sh(network)
        # skip=2, take=2
        return {
            'addresses': response['addresses'][2:4]
        }

    return _partialaddressbook_p2sh


@pytest.fixture(scope='function')
def partialaddressbook_p2wpkh(fulladdressbook_p2wpkh):
    # noinspection PyUnresolvedReferences
    def _partialaddressbook_p2wpkh(network: 'BaseNetwork') -> dict:
        response = fulladdressbook_p2wpkh(network)
        # skip=2, take=2
        return {
            'addresses': response['addresses'][2:4]
        }

    return _partialaddressbook_p2wpkh


@pytest.fixture(scope='function')
def partialaddressbook_p2wsh(fulladdressbook_p2wsh):
    # noinspection PyUnresolvedReferences
    def _partialaddressbook_p2wsh(network: 'BaseNetwork') -> dict:
        response = fulladdressbook_p2wsh(network)
        # skip=2, take=2
        return {
            'addresses': response['addresses'][2:4]
        }

    return _partialaddressbook_p2wsh
