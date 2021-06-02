"""Adds config flow for Zadnego Ale."""
from __future__ import annotations

import asyncio
from typing import Any

from aiohttp.client_exceptions import ClientConnectorError
import async_timeout
import voluptuous as vol
from zadnegoale import ApiError, ZadnegoAle

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import CONF_REGION, DOMAIN, REGIONS  # pylint:disable=unused-import


class ZadnegoAleFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):  # type: ignore[call-arg]
    """Config flow for Zadnego Ale."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle a flow initialized by the user."""
        errors = {}

        websession = async_get_clientsession(self.hass)

        if user_input is not None:
            await self.async_set_unique_id(
                str(REGIONS.index(user_input[CONF_REGION]) + 1)
            )
            self._abort_if_unique_id_configured()

            try:
                zadnegoale = ZadnegoAle(
                    websession, REGIONS.index(user_input[CONF_REGION]) + 1
                )
                with async_timeout.timeout(10):
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
