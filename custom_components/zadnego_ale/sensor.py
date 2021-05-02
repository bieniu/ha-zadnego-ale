"""Support for the Zadnego Ale service."""
from __future__ import annotations

from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
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
    coordinator = hass.data[DOMAIN][entry.entry_id]

    sensors = []
    for sensor in SENSORS:
        sensors.append(ZadnegoAleSensor(coordinator, sensor))

    async_add_entities(sensors, False)


class ZadnegoAleSensor(CoordinatorEntity, SensorEntity):
    """Define an Zadnego Ale sensor."""

    coordinator: ZadnegoAleDataUpdateCoordinator

    def __init__(
        self, coordinator: ZadnegoAleDataUpdateCoordinator, sensor_type: str
    ) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self.sensor_type = sensor_type
        self._attrs = {ATTR_ATTRIBUTION: ATTRIBUTION}

    @property
    def name(self) -> str:
        """Return the name."""
        return f"Stężenie {self.sensor_type.title()}"

    @property
    def state(self) -> StateType:
        return getattr(self.coordinator.data, self.sensor_type, {}).get("level", "brak")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        for attr in ["trend", "value"]:
            self._attrs[attr] = getattr(
                self.coordinator.data, self.sensor_type, {}
            ).get(attr)
        return self._attrs

    @property
    def icon(self) -> str:
        """Return the icon."""
        return SENSORS[self.sensor_type]

    @property
    def unique_id(self) -> str:
        """Return a unique_id for this entity."""
        return f"{self.coordinator.region}-{self.sensor_type}"

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return {
            "identifiers": {(DOMAIN, str(self.coordinator.region))},
            "name": REGIONS[self.coordinator.region - 1],
            "manufacturer": "Żadnego Ale",
            "entry_type": "service",
        }
