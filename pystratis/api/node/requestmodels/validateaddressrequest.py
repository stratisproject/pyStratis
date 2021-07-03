from pystratis.api import Model


class ValidateAddressRequest(Model):
    """A request model for the node/validate-address endpoint.

    Args:
        address (str): The address to validate.
    """
    address: str
