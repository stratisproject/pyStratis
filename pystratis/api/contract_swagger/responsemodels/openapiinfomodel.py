from pystratis.api import Model


# noinspection PyUnresolvedReferences
class OpenAPIInfoModel(Model):
    """A pydantic model for the OpenAPI schema information for deployed smart contracts."""
    title: str
    """The smart contract title."""
    description: str
    """The smart contract description."""
    version: str
    """The smart contract version."""
