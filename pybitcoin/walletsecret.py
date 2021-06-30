from pydantic import BaseModel, Field, SecretStr


class WalletSecret(BaseModel):
    """A model representing credentials of the wallet.
    
    Args:
        wallet_name (str): The name of the wallet.
        wallet_password (SecretStr): The password of the wallet.
    """
    wallet_name: str = Field(alias='walletName')
    wallet_password: SecretStr = Field(alias='walletPassword')

    class Config:
        json_encoders = {
            SecretStr: lambda v: v.get_secret_value()
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
