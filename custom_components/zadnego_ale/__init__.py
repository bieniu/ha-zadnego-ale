"""The Zadnego Ale component."""
import asyncio
import logging

from aiohttp.client_exceptions import ClientConnectorError
from async_timeout import timeout
from zadnegoale import ApiError, ZadnegoAle

from homeassistant.core import Config, HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import CONF_REGION, DEFAULT_UPDATE_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor"]


async def async_setup(  # pylint:disable=unused-argument
    hass: HomeAssistant, config: Config
) -> bool:
    """"Old way of setting up Zadnego Ale integrations."""
    return True


async def async_setup_entry(hass, config_entry):
    """Set up Zadnego Ale as config entry."""
    region = config_entry.data[CONF_REGION]

    websession = async_get_clientsession(hass)

    coordinator = ZadnegoAleDataUpdateCoordinator(hass, websession, region)
    await coordinator.async_refresh()

    if not coordinator.last_update_success:
        raise ConfigEntryNotReady

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][config_entry.entry_id] = coordinator

    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(config_entry, component)
        )

    return True


async def async_unload_entry(hass, config_entry):
    """Unload a config entry."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(config_entry, component)
                for component in PLATFORMS
            ]
        )
    )

    if unload_ok:
        hass.data[DOMAIN].pop(config_entry.entry_id)

    return unload_ok


class ZadnegoAleDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching ZadnegoAle data API."""

    def __init__(self, hass, session, region):
        """Initialize."""
        self.region = region
        self.zadnegoale = ZadnegoAle(session, region)

        super().__init__(
            hass, _LOGGER, name=DOMAIN, update_interval=DEFAULT_UPDATE_INTERVAL
        )

    async def _async_update_data(self):
        """Update data via library."""
        try:
            with timeout(5):
                data = await self.zadnegoale.async_update()
        except (ApiError, ClientConnectorError) as error:
            raise UpdateFailed(error) from error

        return data["sensors"]
