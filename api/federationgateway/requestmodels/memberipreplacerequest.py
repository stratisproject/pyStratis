from pybitcoin import Model


class MemberIPReplaceRequest(Model):
    """A request model for the federationgateway/member/ip/replace endpoint.

    Args:
        endpointtouse (str): The new endpoint.
        endpoint (str): The endpoint being replaced.
    """
    endpointtouse: str
    endpoint: str
