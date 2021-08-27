"""The Zadnego Ale component."""
from __future__ import annotations

import logging
from typing import Final

from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientConnectorError
import async_timeout
from zadnegoale import Allergens, ApiError, ZadnegoAle

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.device_registry import async_get_registry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import CONF_REGION, DEFAULT_UPDATE_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS: Final[list[str]] = ["sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Zadnego Ale as config entry."""
    region = entry.data[CONF_REGION]

    # Migrate unique_id from int to str
    if isinstance(entry.unique_id, int):
        hass.config_entries.async_update_entry(entry, unique_id=str(region))

    # Migrate device_info identifiers from int to str
    device_registry = await async_get_registry(hass)
    old_ids = (DOMAIN, region)
    device_entry = device_registry.async_get_device({old_ids})
    if device_entry and entry.entry_id in device_entry.config_entries:
        new_ids = (DOMAIN, str(region))
        device_registry.async_update_device(device_entry.id, new_identifiers={new_ids})

    websession = async_get_clientsession(hass)

    coordinator = ZadnegoAleDataUpdateCoordinator(hass, websession, region)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    hass.config_entries.async_setup_platforms(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok: bool = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


class ZadnegoAleDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching ZadnegoAle data API."""

    def __init__(
        self, hass: HomeAssistant, session: ClientSession, region: int
    ) -> None:
        """Initialize."""
        self.region = region
        self.zadnegoale = ZadnegoAle(session, region, debug=True)

        super().__init__(
            hass, _LOGGER, name=DOMAIN, update_interval=DEFAULT_UPDATE_INTERVAL
        )

    async def _async_update_data(self) -> Allergens:
        """Update data via library."""
        try:
            with async_timeout.timeout(10):
                return await self.zadnegoale.async_get_dusts()
        except (ApiError, ClientConnectorError) as error:
            raise UpdateFailed(error) from error
