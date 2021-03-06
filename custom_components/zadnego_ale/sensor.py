"""Support for the Zadnego Ale service."""
from __future__ import annotations

import logging
from typing import Any, cast

from homeassistant.components.sensor import (
    DOMAIN as PLATFORM,
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import entity_registry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import ZadnegoAleDataUpdateCoordinator
from .const import (
    ATTR_TREND,
    ATTR_VALUE,
    ATTRIBUTION,
    DOMAIN,
    REGIONS,
    SENSORS,
    SENSORS_MIGRATION,
)

PARALLEL_UPDATES = 1

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Add a Zadnego Ale entities from a config_entry."""
    coordinator: ZadnegoAleDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    # Migrate entity unique_id
    ent_reg = entity_registry.async_get(hass)
    for old_sensor, new_sensor in SENSORS_MIGRATION:
        old_unique_id = f"{coordinator.region}-{old_sensor}"
        new_unique_id = f"{coordinator.region}-{new_sensor}"
        if entity_id := ent_reg.async_get_entity_id(PLATFORM, DOMAIN, old_unique_id):
            _LOGGER.debug(
                "Migrating entity %s from old unique ID '%s' to new unique ID '%s'",
                entity_id,
                old_unique_id,
                new_unique_id,
            )
            ent_reg.async_update_entity(entity_id, new_unique_id=new_unique_id)

    sensors: list[ZadnegoAleSensor] = []
    for description in SENSORS:
        sensors.append(ZadnegoAleSensor(coordinator, description))

    async_add_entities(sensors)


class ZadnegoAleSensor(CoordinatorEntity, SensorEntity):
    """Define an Zadnego Ale sensor."""

    coordinator: ZadnegoAleDataUpdateCoordinator

    def __init__(
        self,
        coordinator: ZadnegoAleDataUpdateCoordinator,
        description: SensorEntityDescription,
    ) -> None:
        """Initialize."""
        super().__init__(coordinator)

        self._attr_device_info = {
            "identifiers": {(DOMAIN, str(coordinator.region))},
            "name": REGIONS[coordinator.region - 1],
            "manufacturer": "??adnego Ale",
            "entry_type": "service",
        }
        self._attr_unique_id = f"{coordinator.region}-{description.key}"
        self._attrs = {ATTR_ATTRIBUTION: ATTRIBUTION}
        self._sensor_data = getattr(coordinator.data, description.key)
        self.entity_description = description

    @property
    def native_value(self) -> StateType:
        """Return the state."""
        return cast(StateType, self._sensor_data.level)

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        for item in (ATTR_TREND, ATTR_VALUE):
            self._attrs[item] = getattr(self._sensor_data, item)

        return self._attrs

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._sensor_data = getattr(self.coordinator.data, self.entity_description.key)
        self.async_write_ha_state()
