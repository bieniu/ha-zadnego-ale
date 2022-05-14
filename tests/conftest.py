"""Global fixtures for zadnego_ale integration."""
import json
from unittest.mock import patch

import pytest
from pytest_homeassistant_custom_component.common import load_fixture

from custom_components.zadnego_ale import ApiError


@pytest.fixture(name="bypass_get_data")
def bypass_get_data_fixture():
    """Skip calls to get data from API."""
    with patch(
        "custom_components.zadnego_ale.ZadnegoAle._async_get_data",
        return_value=json.loads(load_fixture("zadnego_ale_data.json")),
    ):
        yield


@pytest.fixture(name="error_on_get_data")
def error_get_data_fixture():
    """Simulate error when retrieving data from API."""
    with patch(
        "custom_components.zadnego_ale.ZadnegoAle._async_get_data",
        side_effect=ApiError("exception"),
    ):
        yield


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Auto enable custom integrations."""
    yield
