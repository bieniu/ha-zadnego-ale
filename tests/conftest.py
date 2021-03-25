"""Global fixtures for zadnego_ale integration."""
from unittest.mock import patch

import pytest

from custom_components.zadnego_ale import ApiError

@pytest.mark.asyncio
@pytest.fixture(name="bypass_get_data")
def bypass_get_data_fixture():
    """Skip calls to get data from API."""
    with patch("custom_components.zadnego_ale.ZadnegoAle.async_update"):
        yield


@pytest.fixture(name="error_on_get_data")
def error_get_data_fixture():
    """Simulate error when retrieving data from API."""
    with patch(
        "custom_components.zadnego_ale.ZadnegoAle.async_update",
        side_effect=ApiError("exception"),
    ):
        yield
