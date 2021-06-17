# pystratis
Unofficial python package for interacting with Stratis (STRAX) full node and Cirrus/Interflux sidechain.

**Current version: 1.0.9.0** (shadows StratisFullNode)

## Work in progress - TODO
Status: 942 passed, 0 failed, 20 skipped.

DONE
- Pybitcoin networks, types and primatives. Status: All passed.
- API request models and response models. Status: All passed.
- Per endpoint unit tests. Status: All passed.
- Strax integration testing. Status: All passed.
- Cirrus integration testing. Status: Only SC and SCW tests remaining. 

TODO
- Cirrus integration tests: WIP
- Interflux integration tests: Next
- Improve documentation on request models and API methods.
- Generate Sphinx documentation

TESTING GUIDE
- Unit tests: pytest -m "not integration_test"
- Strax integration tests: pytest -m "strax_integration_test"
- Cirrus integration tests: pytest -m "cirrus_integration_test"
- Interflux integration tests: pytest -m "interflux_integration_test"
- Integration tests: pytest -m "integration_test"  
- Everything: pytest
- Coverage: coverage run -m pytest
- Coverage report: coverage report -m
