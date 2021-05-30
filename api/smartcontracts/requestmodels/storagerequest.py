from pydantic import Field, conint
from pybitcoin import Address, Model


class StorageRequest(Model):
    """A StorageRequest."""
    contract_address: Address = Field(alias='ContractAddress')
    storage_key: str = Field(alias='StorageKey')
    data_type: conint(ge=1, le=12)
