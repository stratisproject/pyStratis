import json
from json.decoder import JSONDecodeError
from typing import Any, Union
from requests import get, post, delete, put
from pystratis.api import APIError
from pydantic import BaseModel
from pystratis.core.networks import BaseNetwork
from loguru import logger


class APIRequest:
    """A class for creating an api request and processing the initial response."""
    def __init__(self, network: BaseNetwork, baseuri: str, **kwargs):
        """Initialize the API request handler baseclass."""
        self._network = network
        self._baseuri = baseuri
        self._headers = {'Accept': '*/*', 'Content-Type': 'application/json'}

    def get(self, request_model: Union[BaseModel, dict] = None, **kwargs) -> Any:
        """API get request."""
        if request_model is None:
            params = None
        elif isinstance(request_model, dict):
            params = request_model
        else:
            # Needs to be a dict for use in requests, but use json() to serialize data first.
            params_json = request_model.json()
            params = json.loads(params_json)
        headers = self._headers
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        response = get(
            url=f'{self._baseuri}{kwargs["endpoint"]}',
            params=params,
            headers=headers,
            timeout=60
        )
        if response.status_code == 200:
            if response is not None:
                try:
                    return response.json()
                except JSONDecodeError:
                    return response.text
        else:
            if response is not None:
                try:
                    return logger.debug(response.json())
                except JSONDecodeError:
                    return logger.debug(response.text)
            raise APIError(code=response.status_code, message=response.text)

    def post(self, request_model: Union[BaseModel, dict, str], **kwargs) -> Any:
        """API post request."""
        headers = self._headers
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        if isinstance(request_model, (str, dict)):
            data = json.dumps(request_model)
        else:
            data = request_model.json()
        response = post(
            url=f'{self._baseuri}{kwargs["endpoint"]}',
            data=data,
            headers=headers,
            timeout=60
        )
        if response.status_code == 200:
            if response is not None:
                try:
                    return response.json()
                except JSONDecodeError:
                    return response.text
        else:
            if response is not None:
                try:
                    return logger.debug(response.json())
                except JSONDecodeError:
                    return logger.debug(response.text)
            raise APIError(code=response.status_code, message=response.text)

    def delete(self, request_model: Union[BaseModel, dict] = None, **kwargs) -> Any:
        """API delete request."""
        headers = self._headers
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        if request_model is None:
            params = None
        elif isinstance(request_model, dict):
            params = json.dumps(request_model)
        else:
            # Needs to be a dict for use in requests, but use json() to serialize data first.
            params_json = request_model.json()
            params = json.loads(params_json)
        response = delete(
            url=f'{self._baseuri}{kwargs["endpoint"]}',
            params=params,
            headers=headers,
            timeout=60
        )
        if response.status_code == 200:
            if response is not None:
                try:
                    return response.json()
                except JSONDecodeError:
                    return response.text
        else:
            if response is not None:
                try:
                    return logger.debug(response.json())
                except JSONDecodeError:
                    return logger.debug(response.text)
            raise APIError(code=response.status_code, message=response.text)

    def put(self, request_model: Union[BaseModel, dict] = None, **kwargs) -> Any:
        """API put request."""
        headers = self._headers
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        if request_model is None:
            data = None
        elif isinstance(request_model, dict):
            data = json.dumps(request_model)
        else:
            data = request_model.json()
        response = put(
            url=f'{self._baseuri}{kwargs["endpoint"]}',
            data=data,
            headers=headers,
            timeout=60
        )
        if response.status_code == 200:
            if response is not None:
                try:
                    return response.json()
                except JSONDecodeError:
                    return response.text
        else:
            if response is not None:
                try:
                    return logger.debug(response.json())
                except JSONDecodeError:
                    return logger.debug(response.text)
            raise APIError(code=response.status_code, message=response.text)
