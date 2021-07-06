from pydantic import BaseModel, Field, SecretStr


class WalletSecret(BaseModel):
    """A pydantic model representing credentials of the wallet."""
    wallet_name: str = Field(alias='walletName')
    """The name of the wallet."""
    wallet_password: SecretStr = Field(alias='walletPassword')
    """The wallet password."""

    class Config:
        json_encoders = {
            SecretStr: lambda v: v.get_secret_value()
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
