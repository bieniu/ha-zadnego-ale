"""Test init of Zadnego Ale integration."""
from pytest_homeassistant_custom_component.common import MockConfigEntry, mock_device_registry

from custom_components.zadnego_ale.const import CONF_REGION, DOMAIN
from homeassistant.config_entries import (
    ENTRY_STATE_LOADED,
    ENTRY_STATE_NOT_LOADED,
    ENTRY_STATE_SETUP_RETRY,
)


async def test_config_entry_not_ready(hass, error_on_get_data):
    """Test for setup failure if connection to Zadnego Ale is missing."""
    entry = MockConfigEntry(domain=DOMAIN, data={CONF_REGION: 2})
    entry.add_to_hass(hass)
    await hass.config_entries.async_setup(entry.entry_id)

    assert entry.state == ENTRY_STATE_SETUP_RETRY


async def test_unload_entry(hass):
    """Test successful unload of entry."""
    entry = MockConfigEntry(domain=DOMAIN, data={CONF_REGION: 2})
    entry.add_to_hass(hass)
    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert len(hass.config_entries.async_entries(DOMAIN)) == 1
    assert entry.state == ENTRY_STATE_LOADED

    assert await hass.config_entries.async_unload(entry.entry_id)
    await hass.async_block_till_done()

    assert entry.state == ENTRY_STATE_NOT_LOADED
    assert not hass.data.get(DOMAIN)


async def test_migrate_device_entry(hass, bypass_get_data):
    """Test device_info identifiers migration."""
    config_entry = MockConfigEntry(
        domain=DOMAIN,
        title="Pomorze",
        unique_id=2,
        data={CONF_REGION: 2},
    )
    config_entry.add_to_hass(hass)

    device_reg = mock_device_registry(hass)
    device_entry = device_reg.async_get_or_create(
        config_entry_id=config_entry.entry_id, identifiers={(DOMAIN, 2)}
    )

    await hass.config_entries.async_setup(config_entry.entry_id)
    await hass.async_block_till_done()

    migrated_device_entry = device_reg.async_get_or_create(
        config_entry_id=config_entry.entry_id, identifiers={(DOMAIN, "2")}
    )
    assert device_entry.id == migrated_device_entry.id