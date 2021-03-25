from pytest_homeassistant_custom_component.common import MockConfigEntry
from homeassistant.helpers import entity_registry as er

from custom_components.zadnego_ale.const import ATTRIBUTION, CONF_REGION, DOMAIN

async def test_sensor(hass, bypass_get_data):
    """Test sensor."""
    registry = er.async_get(hass)

    entry = MockConfigEntry(domain=DOMAIN, data={CONF_REGION: 2})
    entry.add_to_hass(hass)
    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    state = hass.states.get("sensor.stezenie_cladosporium")

    assert state
    assert state.state == "bardzo niskie"
    assert state.attributes.get("attribution") == ATTRIBUTION
    assert state.attributes.get("trend") == "bez zmian"
    assert state.attributes.get("value") == 5
    assert state.attributes.get("icon") == "mdi:mushroom-outline"

    entry = registry.async_get("sensor.stezenie_cladosporium")

    assert entry
    assert entry.unique_id == "2-cladosporium"

    state = hass.states.get("sensor.stezenie_cis")

    assert state
    assert state.state == "brak"
    assert state.attributes.get("attribution") == ATTRIBUTION
    assert state.attributes.get("trend") == "wzrost"
    assert state.attributes.get("value") == 1
    assert state.attributes.get("icon") == "mdi:tree"

    entry = registry.async_get("sensor.stezenie_cis")

    assert entry
    assert entry.unique_id == "2-cis"

    state = hass.states.get("sensor.stezenie_trawy")

    assert state
    assert state.state == "brak"
    assert state.attributes.get("attribution") == ATTRIBUTION
    assert state.attributes.get("trend") is None
    assert state.attributes.get("value") is None
    assert state.attributes.get("icon") == "mdi:grass"

    entry = registry.async_get("sensor.stezenie_trawy")

    assert entry
    assert entry.unique_id == "2-trawy"