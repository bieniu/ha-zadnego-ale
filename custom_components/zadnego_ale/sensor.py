"""Support for the Zadnego Ale service."""
from __future__ import annotations

from typing import Any, cast

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import ZadnegoAleDataUpdateCoordinator
from .const import ATTRIBUTION, DOMAIN, REGIONS, SENSORS

PARALLEL_UPDATES = 1


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Add a Zadnego Ale entities from a config_entry."""
    coordinator: ZadnegoAleDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

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
            "identifiers": {(DOMAIN, str(self.coordinator.region))},
            "name": REGIONS[self.coordinator.region - 1],
            "manufacturer": "Żadnego Ale",
            "entry_type": "service",
        }
        self._attr_icon = SENSORS[sensor_type]
        self._attr_name = f"Stężenie {sensor_type.title()}"
        self._attr_unique_id = f"{coordinator.region}-{sensor_type}"
        self._attrs = {ATTR_ATTRIBUTION: ATTRIBUTION}
        self._sensor_data = getattr(coordinator.data, sensor_type)
        self._sensor_type = sensor_type

    @property
    def state(self) -> str:
        return cast(str, getattr(self._sensor_data, "level", "brak"))

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        for attr in ["trend", "value"]:
            self._attrs[attr] = getattr(self._sensor_data, attr, None)
        return self._attrs

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._sensor_data = getattr(self.coordinator.data, self._sensor_type)
        self.async_write_ha_state()
