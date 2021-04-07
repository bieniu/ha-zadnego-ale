"""The Zadnego Ale component."""
import asyncio
import logging
from typing import Any, Optional

from aiohttp.client_exceptions import ClientConnectorError
import async_timeout
from zadnegoale import ApiError, ZadnegoAle

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import CONF_REGION, DEFAULT_UPDATE_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Zadnego Ale as config entry."""
    region = entry.data[CONF_REGION]

    websession = async_get_clientsession(hass)

    coordinator = ZadnegoAleDataUpdateCoordinator(hass, websession, region)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    for platform in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, platform)
        )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
            ]
        )
    )

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


class ZadnegoAleDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching ZadnegoAle data API."""

    def __init__(self, hass, session, region):
        """Initialize."""
        self.region = region
        self.zadnegoale = ZadnegoAle(session, region, debug=True)

        super().__init__(
            hass, _LOGGER, name=DOMAIN, update_interval=DEFAULT_UPDATE_INTERVAL
        )

    async def _async_update_data(self) -> Optional[Any]:
        """Update data via library."""
        try:
            with async_timeout.timeout(10):
                data = await self.zadnegoale.async_update()
        except (ApiError, ClientConnectorError) as error:
            raise UpdateFailed(error) from error

        return data.sensors
