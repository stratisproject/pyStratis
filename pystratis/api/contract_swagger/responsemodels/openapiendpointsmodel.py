from __future__ import annotations
from typing import Callable, List
from .swaggerendpointmodel import SwaggerEndpointModel


# noinspection PyUnresolvedReferences
class OpenAPIEndpointsModel:
    """A model for the OpenAPI schema paths for deployed smart contracts."""

    def __init__(self, response: dict):
        self._endpoints = []
        for key in response:
            method = 'post' if 'post' in response[key] else 'get'
            parameters = response[key][method]['parameters']
            if method == 'post':
                response_body = response[key][method]['requestBody']['content']['application/json']['schema']['properties']
            else:
                response_body = None
            endpoint = SwaggerEndpointModel(
                method=method,
                parameters=parameters,
                response_body=response_body
            )
            self._endpoints.append(endpoint)

    def __repr__(self) -> str:
        return f"OpenAPIPathsModel(endpoints={self.endpoints})"

    def __str__(self) -> str:
        return str(self.endpoints)

    def __eq__(self, other) -> bool:
        return self.endpoints == other

    def json(self) -> str:
        return str(self.endpoints)

    @property
    def endpoints(self) -> List[SwaggerEndpointModel]:
        return self._endpoints

    @classmethod
    def __get_validators__(cls) -> Callable:
        yield cls.validate_class

    @classmethod
    def validate_class(cls, value) -> OpenAPIEndpointsModel:
        cls.validate_values(value)
        return value

    @staticmethod
    def validate_values(values) -> bool:
        if not isinstance(values, OpenAPIEndpointsModel):
            assert isinstance(values, dict)
            for key in values:
                assert isinstance(values[key], dict)
                assert 'get' in values[key] or 'post' in response[key]
        return True

