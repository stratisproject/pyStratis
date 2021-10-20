from __future__ import annotations
from typing import Optional


class SwaggerEndpointModel:
    """A swagger schema path."""

    def __init__(self, method: str, parameters: dict, response_body: dict = None):
        self._method = method
        self._parameters = parameters
        self._response_body = response_body

    def __repr__(self) -> str:
        return f"SwaggerEndpointModel(method={self.method}, parameters={self.parameters}, response_body={self.response_body})"

    def __str__(self) -> str:
        return f"SwaggerEndpointModel(method={self.method}, parameters={self.parameters}, response_body={self.response_body})"

    def __eq__(self, other: SwaggerEndpointModel) -> bool:
        if self.method == other.method and self.parameters == other.parameters and self.response_body == other.response_body:
            return True
        return False

    @property
    def method(self) -> str:
        return self._method

    @property
    def parameters(self) -> dict:
        return self._parameters

    @property
    def response_body(self) -> Optional[dict]:
        return self._response_body
