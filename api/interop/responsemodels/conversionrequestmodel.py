from pydantic import Field, conint
from pybitcoin import Model, Address
from pybitcoin.types import Money, uint256


class ConversionRequestModel(Model):
    """A ConversionRequestModel."""
    request_id: uint256 = Field(alias='requestId')
    request_type: conint(ge=0) = Field(alias='requestType')
    request_status: conint(ge=0) = Field(alias='requestStatus')
    block_height: conint(ge=0) = Field(alias='blockHeight')
    destination_address: Address = Field(alias='destinationAddress')
    amount: Money
    processed: bool
