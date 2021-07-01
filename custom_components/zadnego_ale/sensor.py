"""Support for the Zadnego Ale service."""
from __future__ import annotations

import logging
from typing import Any, cast

from homeassistant.components.sensor import DOMAIN as PLATFORM, SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION, ATTR_DEVICE_CLASS, ATTR_ICON
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import entity_registry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import ZadnegoAleDataUpdateCoordinator
from .const import (
    ATTR_LABEL,
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
    for sensor in SENSORS:
        sensors.append(ZadnegoAleSensor(coordinator, sensor))

    async_add_entities(sensors)


class ZadnegoAleSensor(CoordinatorEntity, SensorEntity):
    """Define an Zadnego Ale sensor."""

    coordinator: ZadnegoAleDataUpdateCoordinator

    def __init__(
        self, coordinator: ZadnegoAleDataUpdateCoordinator, sensor_type: str
    ) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._attr_device_info = {
            "identifiers": {(DOMAIN, str(coordinator.region))},
            "name": REGIONS[coordinator.region - 1],
            "manufacturer": "Żadnego Ale",
            "entry_type": "service",
        }
        description = SENSORS[sensor_type]
        self._attr_device_class = description[ATTR_DEVICE_CLASS]
        self._attr_icon = description[ATTR_ICON]
        self._attr_name = f"{description[ATTR_LABEL]} Pollen Concentration"
        self._attr_unique_id = f"{coordinator.region}-{sensor_type}"
        self._attrs = {ATTR_ATTRIBUTION: ATTRIBUTION}
        self._sensor_data = getattr(coordinator.data, sensor_type)
        self._sensor_type = sensor_type

    @property
    def state(self) -> str:
        return cast(str, self._sensor_data.level)

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        self._attrs[ATTR_TREND] = self._sensor_data.trend
        self._attrs[ATTR_VALUE] = self._sensor_data.value
        return self._attrs

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._sensor_data = getattr(self.coordinator.data, self._sensor_type)
        self.async_write_ha_state()
