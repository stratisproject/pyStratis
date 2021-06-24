from pybitcoin import Model


class MemberIPRemoveRequest(Model):
    """A request model for the federationgateway/member/ip/remove endpoint.

    Args:
        endpoint (str): The endpoint.
    """
    endpoint: str
