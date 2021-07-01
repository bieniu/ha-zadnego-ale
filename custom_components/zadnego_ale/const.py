"""Constants for Zadnego Ale integration."""
from __future__ import annotations

from datetime import timedelta
from typing import Final

from homeassistant.const import ATTR_DEVICE_CLASS, ATTR_ICON

from .model import SensorDescription

ATTRIBUTION: Final = (
    "Dane dostarczone przez Ośrodek Badania Alergenów Środowiskowych Sp. z o.o."
)

ATTR_LABEL: Final = "label"
ATTR_LEVEL: Final = "level"

CONF_REGION: Final = "region"

DEFAULT_NAME: Final = "Żadnego Ale"
DEFAULT_UPDATE_INTERVAL = timedelta(minutes=60)
DOMAIN: Final = "zadnego_ale"

REGIONS: Final[tuple[str, ...]] = (
    "Wybrzeże",
    "Pomorze",
    "Warmia, Mazury i Podlasie",
    "Ziemia Lubuska",
    "Śląsk i Wielkopolska",
    "Mazowsze i Ziemia Łódzka",
    "Małopolska i Ziemia Lubelska",
    "Sudety",
    "Karpaty",
)

SENSORS: Final[dict[str, SensorDescription]] = {
    "alder": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Alder",
    },
    "alternaria": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:mushroom-outline",
        ATTR_LABEL: "Alternaria",
    },
    "ash_tree": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Ash Tree",
    },
    "beech": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Beech",
    },
    "birch_tree": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Birch Tree",
    },
    "cladosporium": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:mushroom-outline",
        ATTR_LABEL: "Cladosporium",
    },
    "elm": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Elm",
    },
    "grass": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:grass",
        ATTR_LABEL: "Grass",
    },
    "hazel": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Hazel",
    },
    "hornbeam": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Hornbeam",
    },
    "maple": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Maple",
    },
    "mugwort": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:sprout",
        ATTR_LABEL: "Mugwort",
    },
    "nettle": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:sprout",
        ATTR_LABEL: "Nettle",
    },
    "oak": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Oak",
    },
    "pigweed": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:sprout",
        ATTR_LABEL: "Pigweed",
    },
    "pine": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:pine-tree",
        ATTR_LABEL: "Pine",
    },
    "plane_tree": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Plane Tree",
    },
    "plantain": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:sprout",
        ATTR_LABEL: "Plantain",
    },
    "poplar": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Poplar",
    },
    "ragweed": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:sprout",
        ATTR_LABEL: "Ragweed",
    },
    "sorrel": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:sprout",
        ATTR_LABEL: "Sorrel",
    },
    "willow": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Willow",
    },
    "yew": {
        ATTR_DEVICE_CLASS: "zadnego_ale__concentration",
        ATTR_ICON: "mdi:tree",
        ATTR_LABEL: "Yew",
    },
}

SENSORS_MIGRATION: Final[list[tuple[str, str]]] = [
    ("ambrozja", "ragweed"),
    ("babka", "plantain"),
    ("brzoza", "birch_tree"),
    ("buk", "beech"),
    ("bylica", "mugwort"),
    ("cis", "yew"),
    ("dąb", "oak"),
    ("grab", "hornbeam"),
    ("jesion", "ash_tree"),
    ("klon", "maple"),
    ("komosa", "pigweed"),
    ("leszczyna", "hazel"),
    ("olsza", "alder"),
    ("platan", "plane_tree"),
    ("pokrzywa", "nettle"),
    ("sosna", "pine"),
    ("szczaw", "sorrel"),
    ("topola", "poplar"),
    ("trawy", "grass"),
    ("wierzba", "willow"),
    ("wiąz", "elm"),
]
