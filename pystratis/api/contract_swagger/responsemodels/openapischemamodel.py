from pystratis.api import Model
from .openapiinfomodel import OpenAPIInfoModel
from .openapiendpointsmodel import OpenAPIEndpointsModel


# noinspection PyUnresolvedReferences
class OpenAPISchemaModel(Model):
    """A pydantic model for the OpenAPI smart contract schema response."""
    openapi: str
    """The OpenAPI version."""
    info: OpenAPIInfoModel
    """Schema information."""
    paths: OpenAPIEndpointsModel
    """Schema endpoint information."""
    components: dict
    """Schema components."""
