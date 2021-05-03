"""Define tests for the Zadnego Ale config flow."""
from unittest.mock import patch

from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.zadnego_ale.const import CONF_REGION, DOMAIN
from homeassistant.config_entries import SOURCE_USER
from homeassistant.data_entry_flow import RESULT_TYPE_CREATE_ENTRY, RESULT_TYPE_FORM

USER_INPUT = {CONF_REGION: "Pomorze"}


async def test_create_entry(hass, bypass_get_data):
    """Test that the user step works."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )

    assert result["type"] == RESULT_TYPE_FORM
    assert result["step_id"] == SOURCE_USER
    assert result["errors"] == {}

    with patch("custom_components.zadnego_ale.async_setup_entry", return_value=True):
        result = await hass.config_entries.flow.async_configure(
            result["flow_id"], user_input=USER_INPUT
        )

        assert result["type"] == RESULT_TYPE_CREATE_ENTRY
        assert result["title"] == "Pomorze"
        assert result["data"][CONF_REGION] == 2


async def test_duplicate_error(hass, bypass_get_data):
    """Test that errors are shown when duplicates are added."""
    entry = MockConfigEntry(domain=DOMAIN, unique_id="2", data={CONF_REGION: 2})
    entry.add_to_hass(hass)

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )

    assert result["type"] == "abort"
    assert result["reason"] == "already_configured"


async def test_failed_config_flow(hass, error_on_get_data):
    """Test a failed config flow due to credential validation failure."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )

    assert result["type"] == RESULT_TYPE_FORM
    assert result["step_id"] == "user"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], user_input=USER_INPUT
    )

    assert result["type"] == RESULT_TYPE_FORM
    assert result["errors"] == {"base": "cannot_connect"}
