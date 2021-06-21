from api import APIRequest, EndpointRegister, endpoint
from api.coldstaking.requestmodels import *
from api.coldstaking.responsemodels import *
from pybitcoin import UtxoDescriptor, AddressDescriptor
from pybitcoin.types import Address, Money, hexstr


class ColdStaking(APIRequest, metaclass=EndpointRegister):
    route = '/api/coldstaking'

    def __init__(self, **kwargs):
        super(ColdStaking, self).__init__(**kwargs)

    @endpoint(f'{route}/cold-staking-info')
    def info(self, request_model: InfoRequest, **kwargs) -> InfoModel:
        """Gets general information related to cold staking.

        Args:
            request_model: InfoRequest model
            **kwargs:

        Returns:
            InfoModel

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)

        return InfoModel(**data)

    @endpoint(f'{route}/cold-staking-account')
    def account(self, request_model: AccountRequest, **kwargs) -> AccountModel:
        """Create a cold staking account.

        Args:
            request_model: AccountRequest model
            **kwargs:

        Returns:
            AccountModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return AccountModel(**data)

    @endpoint(f'{route}/cold-staking-address')
    def address(self, request_model: AddressRequest, **kwargs) -> AddressModel:
        """Gets a cold staking address.

        Args:
            request_model: AddressRequest model
            **kwargs:

        Returns:
            AddressModel

        Raises:
            APIError
        """
        data = self.get(request_model, **kwargs)
        data['address'] = Address(address=data['address'], network=self._network)

        return AddressModel(**data)

    @endpoint(f'{route}/setup-cold-staking')
    def setup(self, request_model: SetupRequest, **kwargs) -> SetupModel:
        """Spends funds from a normal wallet addresses to the cold staking script.

        Args:
            request_model: SetupRequest model
            **kwargs:

        Returns:
            SetupModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)
        data['transactionHex'] = hexstr(data['transactionHex'])

        return SetupModel(**data)

    @endpoint(f'{route}/setup-offline-cold-staking')
    def setup_offline(self, request_model: SetupOfflineRequest, **kwargs) -> BuildOfflineSignModel:
        """Creates a cold staking setup transaction in an unsigned state.

        Args:
            request_model: SetupOfflineRequest model
            **kwargs:

        Returns:
            BuildOfflineSignModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        # Build the UtxoDescriptors
        data['utxos'] = [UtxoDescriptor(**x) for x in data['utxos']]

        # Build the AddressDescriptors
        address_descriptors = []
        for address_descriptor in data['addresses']:
            address_descriptor['address'] = Address(address=address_descriptor['address'], network=self._network)
            address_descriptors.append(address_descriptor)
        data['addresses'] = [AddressDescriptor(**x) for x in address_descriptors]
        data['fee'] = Money.from_satoshi_units(data['fee'])

        return BuildOfflineSignModel(**data)

    @endpoint(f'{route}/estimate-cold-staking-setup-tx-fee')
    def estimate_setup_tx_fee(self, request_model: SetupRequest, **kwargs) -> Money:
        """Estimate the cold staking setup tx fee.

        Args:
            request_model: SetupRequest model
            **kwargs:

        Returns:
            Money

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return Money.from_satoshi_units(data)

    @endpoint(f'{route}/estimate-offline-cold-staking-setup-tx-fee')
    def estimate_offline_setup_tx_fee(self, request_model: SetupOfflineRequest, **kwargs) -> Money:
        """Estimate the cold staking offline setup tx fee.

        Args:
            request_model: SetupOfflineRequest model
            **kwargs:

        Returns:
            Money

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return Money.from_satoshi_units(data)

    @endpoint(f'{route}/cold-staking-withdrawal')
    def withdrawal(self, request_model: WithdrawalRequest, **kwargs) -> WithdrawalModel:
        """Spends funds from the cold staking wallet account back to a normal wallet account.

        Args:
            request_model: WithdrawalRequest model
            **kwargs:

        Returns:
            WithdrawalModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return WithdrawalModel(**data)

    @endpoint(f'{route}/offline-cold-staking-withdrawal')
    def offline_withdrawal(self, request_model: OfflineWithdrawalRequest, **kwargs) -> BuildOfflineSignModel:
        """Builds a request to spend funds from a cold staking wallet account back to a normal wallet account.

        Args:
            request_model: OfflineWithdrawalRequest model
            **kwargs:

        Returns:
            BuildOfflineSignModel

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)
        data['fee'] = Money.from_satoshi_units(data['fee'])

        # Build the UtxoDescriptors
        for i in range(len(data['utxos'])):
            data['utxos'][i]['amount'] = Money(data['utxos'][i]['amount'])
        data['utxos'] = [UtxoDescriptor(**x) for x in data['utxos']]

        # Build the AddressDescriptors
        address_descriptors = []
        for address_descriptor in data['addresses']:
            address_descriptor['address'] = Address(address=address_descriptor['address'], network=self._network)
            address_descriptors.append(address_descriptor)
        data['addresses'] = [AddressDescriptor(**x) for x in address_descriptors]

        return BuildOfflineSignModel(**data)

    @endpoint(f'{route}/estimate-offline-cold-staking-withdrawal-tx-fee')
    def estimate_offline_withdrawal_tx_fee(self, request_model: OfflineWithdrawalFeeEstimationRequest, **kwargs) -> Money:
        """Estimate the fee for an offline cold staking withdrawal transaction.

        Args:
            request_model: A OfflineWithdrawalFeeEstimationRequest model.
            **kwargs:

        Returns:
            Money

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return Money.from_satoshi_units(data)

    @endpoint(f'{route}/estimate-cold-staking-withdrawal-tx-fee')
    def estimate_withdrawal_tx_fee(self, request_model: WithdrawalRequest, **kwargs) -> Money:
        """Estimate the fee for a cold staking withdrawal transaction.

        Args:
            request_model: A WithdrawalRequest model.
            **kwargs:

        Returns:
            Money

        Raises:
            APIError
        """
        data = self.post(request_model, **kwargs)

        return Money.from_satoshi_units(data)
