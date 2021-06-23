from pybitcoin import Model


class RemoveRequest(Model):
    """A request model for the add addressbook endpoint.

    Args:
        label (str): A label for the address to remove.
    """
    label: str
