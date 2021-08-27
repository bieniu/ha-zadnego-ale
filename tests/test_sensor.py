"""Test sensor of Zadnego Ale integration."""
from datetime import timedelta
import json
from unittest.mock import patch

from pytest_homeassistant_custom_component.common import (
    MockConfigEntry,
    async_fire_time_changed,
    load_fixture,
)

from custom_components.zadnego_ale.const import ATTRIBUTION, CONF_REGION, DOMAIN
from homeassistant.helpers import entity_registry as er
from homeassistant.util.dt import utcnow


async def test_sensor(hass, bypass_get_data):
    """Test sensor."""
    registry = er.async_get(hass)

    entry = MockConfigEntry(domain=DOMAIN, data={CONF_REGION: 2})
    entry.add_to_hass(hass)
    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    state = hass.states.get("sensor.cladosporium_pollen_concentration")

    assert state
    assert state.state == "very low"
    assert state.attributes.get("attribution") == ATTRIBUTION
    assert state.attributes.get("trend") == "steady"
    assert state.attributes.get("value") == 5
    assert state.attributes.get("icon") == "mdi:mushroom-outline"
    assert state.attributes.get("device_class") == "zadnego_ale__concentration"

    entry = registry.async_get("sensor.cladosporium_pollen_concentration")

    assert entry
    assert entry.unique_id == "2-cladosporium"

    state = hass.states.get("sensor.yew_pollen_concentration")

    assert state
    assert state.state == "lack"
    assert state.attributes.get("attribution") == ATTRIBUTION
    assert state.attributes.get("trend") == "rising"
    assert state.attributes.get("value") == 1
    assert state.attributes.get("icon") == "mdi:tree"
    assert state.attributes.get("device_class") == "zadnego_ale__concentration"

    entry = registry.async_get("sensor.yew_pollen_concentration")

    assert entry
    assert entry.unique_id == "2-yew"

    state = hass.states.get("sensor.grass_pollen_concentration")

    assert state
    assert state.state == "lack"
    assert state.attributes.get("attribution") == ATTRIBUTION
    assert state.attributes.get("trend") is None
    assert state.attributes.get("value") == 0
    assert state.attributes.get("icon") == "mdi:grass"
    assert state.attributes.get("device_class") == "zadnego_ale__concentration"

    entry = registry.async_get("sensor.grass_pollen_concentration")

    assert entry
    assert entry.unique_id == "2-grass"

    state = hass.states.get("sensor.plane_tree_pollen_concentration")

    assert state
    assert state.state == "lack"
    assert state.attributes.get("attribution") == ATTRIBUTION
    assert state.attributes.get("trend") == "rising"
    assert state.attributes.get("value") == 1
    assert state.attributes.get("icon") == "mdi:tree"
    assert state.attributes.get("device_class") == "zadnego_ale__concentration"

    entry = registry.async_get("sensor.plane_tree_pollen_concentration")

    assert entry
    assert entry.unique_id == "2-plane_tree"

    state = hass.states.get("sensor.maple_pollen_concentration")

    assert state
    assert state.state == "very low"
    assert state.attributes.get("attribution") == ATTRIBUTION
    assert state.attributes.get("trend") == "steady"
    assert state.attributes.get("value") == 5
    assert state.attributes.get("icon") == "mdi:tree"
    assert state.attributes.get("device_class") == "zadnego_ale__concentration"

    entry = registry.async_get("sensor.maple_pollen_concentration")

    assert entry
    assert entry.unique_id == "2-maple"

    state = hass.states.get("sensor.hornbeam_pollen_concentration")

    assert state
    assert state.state == "medium"
    assert state.attributes.get("attribution") == ATTRIBUTION
    assert state.attributes.get("trend") == "rising"
    assert state.attributes.get("value") == 20
    assert state.attributes.get("icon") == "mdi:tree"
    assert state.attributes.get("device_class") == "zadnego_ale__concentration"

    entry = registry.async_get("sensor.hornbeam_pollen_concentration")

    assert entry
    assert entry.unique_id == "2-hornbeam"


async def test_state_update(hass, bypass_get_data):
    """Ensure the sensor state changes after updating the data."""
    entry = MockConfigEntry(domain=DOMAIN, data={CONF_REGION: 2})
    entry.add_to_hass(hass)
    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    state = hass.states.get("sensor.cladosporium_pollen_concentration")

    assert state
    assert state.state == "very low"

    future = utcnow() + timedelta(minutes=90)

    dusts = json.loads(load_fixture("zadnego_ale_data.json"))
    dusts[0]["level"] = "Bardzo wysokie"

    with patch(
        "custom_components.zadnego_ale.ZadnegoAle._async_get_data", return_value=dusts
    ):
        async_fire_time_changed(hass, future)
        await hass.async_block_till_done()

        state = hass.states.get("sensor.cladosporium_pollen_concentration")
        assert state
        assert state.state == "very high"
