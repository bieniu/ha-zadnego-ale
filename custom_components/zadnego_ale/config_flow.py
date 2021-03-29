"""Adds config flow for Zadnego Ale."""
import asyncio
from typing import Optional

from aiohttp.client_exceptions import ClientConnectorError
import async_timeout
import voluptuous as vol
from zadnegoale import ApiError, ZadnegoAle

from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import CONF_REGION, DOMAIN, REGIONS  # pylint:disable=unused-import


class ZadnegoAleFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Zadnego Ale."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize."""
        self._errors = {}

    async def async_step_user(self, user_input: Optional[dict] = None) -> dict:
        """Handle a flow initialized by the user."""
        errors = {}

        websession = async_get_clientsession(self.hass)

        if user_input is not None:
            await self.async_set_unique_id(REGIONS.index(user_input[CONF_REGION]) + 1)
            self._abort_if_unique_id_configured()

            try:
                zadnegoale = ZadnegoAle(
                    websession, REGIONS.index(user_input[CONF_REGION]) + 1
                )
                with async_timeout.timeout(5):
                    await zadnegoale.async_update()
            except (ApiError, ClientConnectorError, asyncio.TimeoutError):
                errors["base"] = "cannot_connect"
            else:
                return self.async_create_entry(
                    title=user_input[CONF_REGION],
                    data={CONF_REGION: REGIONS.index(user_input[CONF_REGION]) + 1},
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required(CONF_REGION): vol.In(REGIONS)}),
            errors=errors,
        )
