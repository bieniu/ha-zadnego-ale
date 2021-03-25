"""Test Zadnego Ale system health."""
import asyncio

from aiohttp import ClientError
from pytest_homeassistant_custom_component.common import get_system_health_info

from custom_components.zadnego_ale.const import DOMAIN
from homeassistant.setup import async_setup_component


async def test_zadnego_ale_system_health(hass, aioclient_mock):
    """Test Zadnego Ale system health."""
    aioclient_mock.get("http://api.zadnegoale.pl", text="")
    hass.config.components.add(DOMAIN)
    assert await async_setup_component(hass, "system_health", {})

    info = await get_system_health_info(hass, DOMAIN)

    for key, val in info.items():
        if asyncio.iscoroutine(val):
            info[key] = await val

    assert info == {"can_reach_server": "ok"}


async def test_zadnego_ale_system_health_fail(hass, aioclient_mock):
    """Test Zadnego Ale system health."""
    aioclient_mock.get("http://api.zadnegoale.pl", exc=ClientError)
    hass.config.components.add(DOMAIN)
    assert await async_setup_component(hass, "system_health", {})

    info = await get_system_health_info(hass, DOMAIN)

    for key, val in info.items():
        if asyncio.iscoroutine(val):
            info[key] = await val

    assert info == {"can_reach_server": {"type": "failed", "error": "unreachable"}}
