from typing import Any
from requests import get, post, delete, put
from api import APIError
from pydantic import BaseModel
from pybitcoin.networks import BaseNetwork


class APIRequest:
    """A class for creating an api request and processing the initial response."""
    def __init__(self, network: BaseNetwork, baseuri: str, **kwargs):
        self._network = network
        self._baseuri = baseuri
        self._headers = {'Accept': '*/*', 'Content-Type': 'application/json'}

    def get(self, request_model: BaseModel = None, **kwargs) -> Any:
        """API get request."""
        response = get(
            url=f'{self._baseuri}{kwargs["endpoint"]}',
            params=None if request_model is None else request_model.json(),
            headers=self._headers,
            timeout=5
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise APIError(code=response.status_code, message=response.text)

    def post(self, request_model: BaseModel, **kwargs) -> Any:
        """API post request."""
        response = post(
            url=f'{self._baseuri}{kwargs["endpoint"]}',
            params=request_model.json(),
            headers=self._headers,
            timeout=5
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise APIError(code=response.status_code, message=response.text)

    def delete(self, request_model: BaseModel, **kwargs) -> Any:
        """API delete request."""
        response = delete(
            url=f'{self._baseuri}{kwargs["endpoint"]}',
            params=request_model.json(),
            headers=self._headers,
            timeout=5
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise APIError(code=response.status_code, message=response.text)

    def put(self, request_model: BaseModel = None, **kwargs) -> Any:
        """API put request."""
        response = put(
            url=f'{self._baseuri}{kwargs["endpoint"]}',
            params=None if request_model is None else request_model.json(),
            headers=self._headers,
            timeout=5
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise APIError(code=response.status_code, message=response.text)
