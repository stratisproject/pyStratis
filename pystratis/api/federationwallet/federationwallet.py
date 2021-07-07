from typing import List, Union
from pystratis.api import APIRequest, EndpointRegister, endpoint
from pystratis.api.federationwallet.requestmodels import *
from pystratis.api.federationwallet.responsemodels import *
from pystratis.core.types import Address, Money, uint256


class FederationWallet(APIRequest, metaclass=EndpointRegister):
    """Implements the federationwallet api endpoints."""

    route = '/api/federationwallet'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/general-info')
    def general_info(self, **kwargs) -> WalletGeneralInfoModel:
        """Retrieves general information about the wallet.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            WalletGeneralInfoModel: General information about the federation wallet.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        return WalletGeneralInfoModel(**data)

    @endpoint(f'{route}/balance')
    def balance(self, **kwargs) -> WalletBalanceModel:
        """Retrieves wallet balances.

        Args:
            **kwargs: Extra keyword arguments. 

        Returns:
            WalletBalanceModel: Federation wallet balance information.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        data = self.get(**kwargs)
        for i in range(len(data['balances'])):
            if data['balances'][i]['amountConfirmed'] is not None:
                data['balances'][i]['amountConfirmed'] = Money.from_satoshi_units(data['balances'][i]['amountConfirmed'])
            if data['balances'][i]['amountUnconfirmed'] is not None:
                data['balances'][i]['amountUnconfirmed'] = Money.from_satoshi_units(data['balances'][i]['amountUnconfirmed'])
            if data['balances'][i]['spendableAmount'] is not None:
                data['balances'][i]['spendableAmount'] = Money.from_satoshi_units(data['balances'][i]['spendableAmount'])
            if data['balances'][i]['addresses'] is not None:
                for j in range(len(data['balances'][i]['addresses'])):
                    if data['balances'][i]['addresses'][j]['amountConfirmed'] is not None:
                        data['balances'][i]['addresses'][j]['amountConfirmed'] = Money.from_satoshi_units(data['balances'][i]['addresses'][j]['amountConfirmed'])
                    if data['balances'][i]['addresses'][j]['amountUnconfirmed'] is not None:
                        data['balances'][i]['addresses'][j]['amountUnconfirmed'] = Money.from_satoshi_units(data['balances'][i]['addresses'][j]['amountUnconfirmed'])
                    data['balances'][i]['addresses'][j]['address'] = Address(address=data['balances'][i]['addresses'][j]['address'], network=self._network)
        return WalletBalanceModel(**data)

    @endpoint(f'{route}/history')
    def history(self, max_entries_to_return: int, **kwargs) -> List[WithdrawalModel]:
        """Retrieves a withdrawal history for the wallet.

        Args:
            max_entries_to_return (int): The maximum number of history entries to return.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[WithdrawalModel]: The federation wallet history.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = HistoryRequest(max_entries_to_return=max_entries_to_return)
        data = self.get(request_model, **kwargs)
        for i in range(len(data)):
            data[i]['amount'] = Money.from_satoshi_units(data[i]['amount'])
            if data[i]['payingTo'] != 'Rewards':
                data[i]['payingTo'] = Address(address=data[i]['payingTo'], network=self._network)
        return [WithdrawalModel(**x) for x in data]

    @endpoint(f'{route}/sync')
    def sync(self, block_hash: Union[str, uint256], **kwargs) -> None:
        """Starts sending block to wallet for synchronisation. Demo/testing use only.

        Args:
            block_hash (uint256, str): The block hash at which to start sync.
            **kwargs: Extra keyword arguments. 

        Returns:
            None

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        if isinstance(block_hash, str):
            block_hash = uint256(block_hash)
        request_model = SyncRequest(block_hash=block_hash)
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/enable-federation')
    def enable_federation(self,
                          mnemonic: str,
                          password: str,
                          passphrase: str = None,
                          timeout_seconds: int = 60,
                          **kwargs) -> Union[None, str]:
        """Enables the federation so that it can sign transactions.

        Args:
            mnemonic (str): The mnemonic.
            password (str): The password.
            passphrase (str, optional): The passphrase.
            timeout_seconds (int, optional): Seconds to timeout. Default=60.
            **kwargs: Extra keyword arguments. 

        Returns:
            (str, None): None if successful, str if error.

        Raises:
            APIError
        """
        request_model = EnableFederationRequest(mnemonic=mnemonic, password=password, passphrase=passphrase, timeout_seconds=timeout_seconds)
        data = self.post(request_model, **kwargs)
        if data is not None:
            return data

    @endpoint(f'{route}/remove-transactions')
    def remove_transactions(self, resync: bool = True, **kwargs) -> List[RemovedTransactionModel]:
        """Remove all transactions from the wallet.

        Args:
            resync (bool, optional): A flag to resync the wallet after transactions are removed. Default=True.
            **kwargs: Extra keyword arguments. 

        Returns:
            List[RemovedTransactionModel]: A list of removed transactions from the federation wallet.

        Raises:
            APIError: Error thrown by node API. See message for details.
        """
        request_model = RemoveTransactionsRequest(resync=resync)
        data = self.delete(request_model, **kwargs)
        return [RemovedTransactionModel(**x) for x in data]
