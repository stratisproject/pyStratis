from typing import Optional
from pydantic import SecretStr
from pybitcoin import Model


class CreateRequest(Model):
    """A request model used for the /wallet/create endpoint.

    Args:
        mnemonic (str, optional): The mnemonic used to create a HD wallet. If not specified, it will be randomly generated underhood.
        password (SecretStr): The password for wallet to be created.
        passphrase (SecretStr): The passphrase used in master key generation.
        name: (str): The name for a wallet to be created.
    """
    mnemonic: Optional[str]
    password: SecretStr
    passphrase: SecretStr
    name: str
