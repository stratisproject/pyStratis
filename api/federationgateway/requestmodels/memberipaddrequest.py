from pybitcoin import Model


class MemberIPAddRequest(Model):
    """A request model for the federationgateway/member/ip/add endpoint.

    Args:
        endpoint (str): The endpoint.
    """
    endpoint: str
