from pystratis.api import Model


class RemoveRequest(Model):
    """A request model for the addressbook/address endpoint.

    Args:
        label (str): A label for the address to remove.
    """
    label: str
