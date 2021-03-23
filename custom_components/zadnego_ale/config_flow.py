"""Adds config flow for Zadnego Ale."""
from zadnegoale import ApiError, ZadnegoAle
import async_timeout
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import CONF_REGION, DOMAIN, REGIONS


class ZadnegoAleFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Zadnego Ale."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize."""
        self._errors = {}

    async def async_step_user(self, user_input=None):
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
            except ApiError:
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
