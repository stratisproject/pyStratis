from pydantic import Field, BaseModel
from pybitcoin.types.address import Address


class AddressDescriptor(BaseModel):
    """An AddressDescriptor"""
    address: Address
    key_path: str = Field(alias='keyPath')
    address_type: str = Field(alias='addressType')

    class Config:
        json_encoders = {
            Address: lambda v: str(v)
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(by_alias=True)
