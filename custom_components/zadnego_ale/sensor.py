"""Support for the Zadnego Ale service."""
from __future__ import annotations

import logging
from typing import Any

from zadnegoale.model import Allergen

from homeassistant.components.sensor import (
    DOMAIN as PLATFORM,
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import entity_registry
from homeassistant.helpers.entity import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
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

    _attr_attribution = ATTRIBUTION
    coordinator: ZadnegoAleDataUpdateCoordinator

    def __init__(
        self,
        coordinator: ZadnegoAleDataUpdateCoordinator,
        description: SensorEntityDescription,
    ) -> None:
        """Initialize."""
        super().__init__(coordinator)

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(coordinator.region))},
            name=REGIONS[coordinator.region - 1],
            manufacturer="Żadnego Ale",
            entry_type=DeviceEntryType.SERVICE,
        )
        self._attr_unique_id = f"{coordinator.region}-{description.key}"
        sensor_data = getattr(coordinator.data, description.key)
        self._attr_native_value = sensor_data.level
        self._attr_extra_state_attributes = _extract_attributes(sensor_data)
        self.entity_description = description

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        sensor_data = getattr(self.coordinator.data, self.entity_description.key)
        self._attr_native_value = sensor_data.level
        self._attr_extra_state_attributes = _extract_attributes(sensor_data)
        self.async_write_ha_state()


@callback
def _extract_attributes(sensor_data: Allergen) -> dict[str, Any]:
    """Extract attributes from sensor data."""
    return {item: getattr(sensor_data, item) for item in (ATTR_TREND, ATTR_VALUE)}
