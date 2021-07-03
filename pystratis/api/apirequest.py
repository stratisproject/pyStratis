import json
from json.decoder import JSONDecodeError
from typing import Any
from requests import get, post, delete, put
from pystratis.api import APIError
from pydantic import BaseModel
from pystratis.core.networks import BaseNetwork


class APIRequest:
    """A class for creating an api request and processing the initial response."""
    def __init__(self, network: BaseNetwork, baseuri: str, **kwargs):
        """Initialize the API request handler baseclass."""
        self._network = network
        self._baseuri = baseuri
        self._headers = {'Accept': '*/*', 'Content-Type': 'application/json'}

    def get(self, request_model: BaseModel = None, **kwargs) -> Any:
        """API get request."""
        if request_model is None:
            params = None
        else:
            # Needs to be a dict for use in requests, but use json() to serialize data first.
            params_json = request_model.json()
            params = json.loads(params_json)
        response = get(
            url=f'{self._baseuri}{kwargs["endpoint"]}',
            params=params,
            headers=self._headers,
            timeout=60
        )
        if response.status_code == 200:
            if response is not None:
                try:
                    return response.json()
                except JSONDecodeError:
                    return response.text
        else:
            print(response.text)
            raise APIError(code=response.status_code, message=response.text)

    def post(self, request_model: BaseModel, **kwargs) -> Any:
        """API post request."""
        response = post(
            url=f'{self._baseuri}{kwargs["endpoint"]}',
            data=request_model.json(),
            headers=self._headers,
            timeout=60
        )
        if response.status_code == 200:
            if response is not None:
                try:
                    return response.json()
                except JSONDecodeError:
                    return response.text
        else:
            print(response.text)
            raise APIError(code=response.status_code, message=response.text)

    def delete(self, request_model: BaseModel, **kwargs) -> Any:
        """API delete request."""
        if request_model is None:
            params = None
        else:
            # Needs to be a dict for use in requests, but use json() to serialize data first.
            params_json = request_model.json()
            params = json.loads(params_json)
        response = delete(
            url=f'{self._baseuri}{kwargs["endpoint"]}',
            params=params,
            headers=self._headers,
            timeout=60
        )
        if response.status_code == 200:
            if response is not None:
                try:
                    return response.json()
                except JSONDecodeError:
                    return response.text
        else:
            print(response.text)
            raise APIError(code=response.status_code, message=response.text)

    def put(self, request_model: BaseModel = None, **kwargs) -> Any:
        """API put request."""
        response = put(
            url=f'{self._baseuri}{kwargs["endpoint"]}',
            data=None if request_model is None else request_model.json(),
            headers=self._headers,
            timeout=60
        )
        if response.status_code == 200:
            if response is not None:
                try:
                    return response.json()
                except JSONDecodeError:
                    return response.text
        else:
            print(response.text)
            raise APIError(code=response.status_code, message=response.text)
