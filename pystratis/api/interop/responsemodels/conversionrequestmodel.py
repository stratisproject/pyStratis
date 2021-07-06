from pydantic import Field
from pystratis.api import Model
from pystratis.core import ConversionRequestType
from pystratis.core.types import Address, Money, uint256


class ConversionRequestModel(Model):
    """A pydantic model of a conversion request."""
    request_id: uint256 = Field(alias='requestId')
    """The hash of the conversion request."""
    request_type: ConversionRequestType = Field(alias='requestType')
    """The conversion request type."""
    request_status: int = Field(alias='requestStatus')
    """The conversion request status."""
    block_height: int = Field(alias='blockHeight')
    """The block height of the transaction."""
    destination_address: Address = Field(alias='destinationAddress')
    """The destination address."""
    amount: Money
    """The amount converted."""
    processed: bool
    """True if the conversion has been processed."""
