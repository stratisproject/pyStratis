from pydantic import SecretStr, BaseModel


class MultisigSecret(BaseModel):
    """A MultisigSecret."""
    mnemonic: SecretStr
    passphrase: SecretStr

    class Config:
        json_encoders = {
            SecretStr: lambda v: v.get_secret_value()
        }
        allow_population_by_field_name = True
