"""Type definitions for Zadnego Ale integration."""
from __future__ import annotations

from typing import TypedDict


class SensorDescription(TypedDict):
    """Sensor description class."""

    device_class: str
    icon: str
    label: str
