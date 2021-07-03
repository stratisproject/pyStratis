import pytest
from pystratis.api.interop.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_status(interflux_cirrusminer_node):
    response = interflux_cirrusminer_node.interop.status()
    assert isinstance(response, StatusModel)
