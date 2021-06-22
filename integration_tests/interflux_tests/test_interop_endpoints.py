import pytest
from api.interop.responsemodels import *


@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_status(interflux_strax_node):
    response = interflux_strax_node.interop.status()
    assert isinstance(response, StatusModel)
