import pytest


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_join_federation():
    # This method is present in the cirrus node but needs to be tested in interflux federation because it requires querying counter chain.
    pass
