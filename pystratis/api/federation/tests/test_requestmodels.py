import json
from pystratis.api.federation.requestmodels import *


def test_atheightrequest(generate_compressed_pubkey):
    data = {
        'blockHeight': 1
    }
    request_model = AtHeightRequest(
        block_height=data['blockHeight']
    )
    assert json.dumps(data) == request_model.json()
