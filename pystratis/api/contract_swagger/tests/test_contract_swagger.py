import pytest
from pytest_mock import MockerFixture
from pystratis.api.contract_swagger import ContractSwagger
from pystratis.api.contract_swagger.responsemodels import OpenAPISchemaModel
from pystratis.core.networks import CirrusMain
from pystratis.core.types import Address


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_address(mocker: MockerFixture, network, generate_p2pkh_address):
    sct_address = generate_p2pkh_address(network=network)
    default_sender = generate_p2pkh_address(network=network)
    default_wallet = 'DefaultWallet'
    fake_method = 'FakeMethod'
    fake_property = 'FakeProperty'
    data = {
      "openapi": "3.0.1",
      "info": {
        "title": "Fake Contract API",
        "description": f"{sct_address}",
        "version": "1"
      },
      "paths": {
        f"/api/contract/{sct_address}/method/{fake_method}": {
          "post": {
            "tags": [
              f"{fake_method}"
            ],
            "operationId": f"{fake_method}",
            "parameters": [
              {
                "name": "GasPrice",
                "in": "header",
                "required": True,
                "schema": {
                  "maximum": 10000,
                  "minimum": 1,
                  "type": "number",
                  "format": "int64",
                  "default": 100
                }
              },
              {
                "name": "GasLimit",
                "in": "header",
                "required": True,
                "schema": {
                  "maximum": 250000,
                  "minimum": 10000,
                  "type": "number",
                  "format": "int64",
                  "default": 10000
                }
              },
              {
                "name": "Amount",
                "in": "header",
                "required": True,
                "schema": {
                  "type": "string",
                  "default": "0"
                }
              },
              {
                "name": "FeeAmount",
                "in": "header",
                "required": True,
                "schema": {
                  "type": "string",
                  "default": "0.01"
                }
              },
              {
                "name": "WalletName",
                "in": "header",
                "required": True,
                "schema": {
                  "type": "string",
                  "default": f"{default_wallet}"
                }
              },
              {
                "name": "WalletPassword",
                "in": "header",
                "required": True,
                "schema": {
                  "type": "string"
                }
              },
              {
                "name": "Sender",
                "in": "header",
                "required": True,
                "schema": {
                  "type": "string",
                  "default": f"{default_sender}"
                }
              }
            ],
            "requestBody": {
              "description": f"{fake_method}",
              "content": {
                "application/json": {
                  "schema": {
                    "title": f"{fake_method}",
                    "properties": {
                      "address": {
                        "type": "string"
                      }
                    }
                  }
                }
              },
              "required": True
            },
            "responses": {
              "200": {
                "description": "Success"
              }
            }
          }
        },
        f"/api/contract/{sct_address}/property/{fake_property}": {
          "get": {
            "tags": [
              f"{fake_property}"
            ],
            "operationId": f"{fake_property}",
            "parameters": [
              {
                "name": "GasPrice",
                "in": "header",
                "required": True,
                "schema": {
                  "maximum": 10000,
                  "minimum": 1,
                  "type": "number",
                  "format": "int64",
                  "default": 100
                }
              },
              {
                "name": "GasLimit",
                "in": "header",
                "required": True,
                "schema": {
                  "maximum": 250000,
                  "minimum": 10000,
                  "type": "number",
                  "format": "int64",
                  "default": 250000
                }
              },
              {
                "name": "Amount",
                "in": "header",
                "required": True,
                "schema": {
                  "type": "string",
                  "default": "0"
                }
              },
              {
                "name": "Sender",
                "in": "header",
                "required": True,
                "schema": {
                  "type": "string",
                  "default": f"{default_sender}"
                }
              }
            ],
            "responses": {
              "200": {
                "description": "Success"
              }
            }
          }
        },
      },
      "components": {}
    }
    mocker.patch.object(ContractSwagger, 'get', return_value=data)
    contract_swagger = ContractSwagger(network=network, baseuri=mocker.MagicMock())

    response = contract_swagger.address(address=sct_address)

    assert response == OpenAPISchemaModel(**data)
    # noinspection PyUnresolvedReferences
    contract_swagger.get.assert_called_once()


@pytest.mark.parametrize('network', [CirrusMain()], ids=['CirrusMain'])
def test_call(mocker: MockerFixture, network, generate_p2pkh_address):
    sct_address = Address(address=generate_p2pkh_address(network=network), network=network)
    mocker.patch.object(ContractSwagger, 'post', return_value=None)
    contract_swagger = ContractSwagger(network=network, baseuri=mocker.MagicMock())

    contract_swagger(address=sct_address)

    # noinspection PyUnresolvedReferences
    contract_swagger.post.assert_called_once()
