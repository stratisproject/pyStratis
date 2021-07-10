from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class StorageRequest(Model):
    """A request model for the smartcontracts/storage endpoint.

    Args:
        contract_address (Address): The smart contract address being called.
        storage_key (str): The key in the key-value store.
        data_type: The data type. Allowed values: [1,12]

    Notes:
        Data_type enumerations: https://academy.stratisplatform.com/Architecture%20Reference/SmartContracts/working-with-contracts.html#parameter-serialization
    """
    contract_address: Address = Field(alias='ContractAddress')
    storage_key: str = Field(alias='StorageKey')
    data_type: conint(ge=1, le=12) = Field(alias='DataType')
