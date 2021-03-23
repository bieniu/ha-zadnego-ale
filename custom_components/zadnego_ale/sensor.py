"""Support for the Zadnego Ale service."""
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import ATTR_ICON, DOMAIN, REGIONS, SENSORS


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add a Zadnego Ale entities from a config_entry."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]

    sensors = []
    for sensor in SENSORS:
        sensors.append(ZadnegoAleSensor(coordinator, sensor))

    async_add_entities(sensors, False)


class ZadnegoAleSensor(CoordinatorEntity):
    """Define an Zadnego Ale sensor."""

    def __init__(self, coordinator, sensor_type):
        """Initialize."""
        super().__init__(coordinator)
        self.sensor_type = sensor_type

    @property
    def name(self):
        """Return the name."""
        return f"Stężenie {self.sensor_type.title()}"

    @property
    def state(self):
        """Return the state."""
        return self.coordinator.data.get(self.sensor_type, {}).get("level", "brak")

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            attr: self.coordinator.data.get(self.sensor_type, {}).get(attr)
            for attr in ["trend", "value"]
        }

    @property
    def icon(self):
        """Return the icon."""
        return SENSORS[self.sensor_type][ATTR_ICON]

    @property
    def unique_id(self):
        """Return a unique_id for this entity."""
        return f"{self.coordinator.region}-{self.sensor_type}"

    @property
    def device_info(self):
        """Return the device info."""
        return {
            "identifiers": {(DOMAIN, self.coordinator.region)},
            "name": REGIONS[self.coordinator.region - 1],
            "manufacturer": "Żadnego Ale",
            "entry_type": "service",
        }
