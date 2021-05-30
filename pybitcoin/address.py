from pydantic import BaseModel, validator
from pybitcoin.networks import BaseNetwork


class Address(BaseModel):
    """A address model. Address is validated by the network."""
    address: str
    network: BaseNetwork

    def __repr__(self) -> str:
        return self.address

    def __str__(self) -> str:
        return self.address

    def __eq__(self, other):
        return self.address == other

    class Config:
        json_encoders = {
            bytes: lambda v: v.hex()
        }
        allow_population_by_field_name = True

    # noinspection PyMethodParameters
    @validator('network')
    def validate_address(cls, v, values):
        if v.validate_address(values['address']):
            return v
        raise ValueError('Invalid address.')
