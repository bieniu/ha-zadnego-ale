"""Constants for Zadnego Ale integration."""
from __future__ import annotations

from datetime import timedelta
from typing import Final

from homeassistant.components.sensor import SensorEntityDescription

ATTRIBUTION: Final = (
    "Dane dostarczone przez Ośrodek Badania Alergenów Środowiskowych Sp. z o.o."
)

ATTR_LEVEL: Final = "level"
ATTR_TREND: Final = "trend"
ATTR_VALUE: Final = "value"

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

SENSORS: Final[tuple[SensorEntityDescription, ...]] = (
    SensorEntityDescription(
        key="alder",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Alder pollen concentration",
    ),
    SensorEntityDescription(
        key="alternaria",
        device_class="zadnego_ale__concentration",
        icon="mdi:mushroom-outline",
        name="Alternaria pollen concentration",
    ),
    SensorEntityDescription(
        key="ash_tree",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Ash Tree pollen concentration",
    ),
    SensorEntityDescription(
        key="beech",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Beech pollen concentration",
    ),
    SensorEntityDescription(
        key="birch_tree",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Birch Tree pollen concentration",
    ),
    SensorEntityDescription(
        key="cladosporium",
        device_class="zadnego_ale__concentration",
        icon="mdi:mushroom-outline",
        name="Cladosporium pollen concentration",
    ),
    SensorEntityDescription(
        key="elm",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Elm pollen concentration",
    ),
    SensorEntityDescription(
        key="goldenrod",
        device_class="zadnego_ale__concentration",
        icon="mdi:grass",
        name="Goldenrod pollen concentration",
    ),
    SensorEntityDescription(
        key="grass",
        device_class="zadnego_ale__concentration",
        icon="mdi:grass",
        name="Grass pollen concentration",
    ),
    SensorEntityDescription(
        key="hazel",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Hazel pollen concentration",
    ),
    SensorEntityDescription(
        key="hornbeam",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Hornbeam pollen concentration",
    ),
    SensorEntityDescription(
        key="maple",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Maple pollen concentration",
    ),
    SensorEntityDescription(
        key="mugwort",
        device_class="zadnego_ale__concentration",
        icon="mdi:sprout",
        name="Mugwort pollen concentration",
    ),
    SensorEntityDescription(
        key="nettle",
        device_class="zadnego_ale__concentration",
        icon="mdi:sprout",
        name="Nettle pollen concentration",
    ),
    SensorEntityDescription(
        key="oak",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Oak pollen concentration",
    ),
    SensorEntityDescription(
        key="pigweed",
        device_class="zadnego_ale__concentration",
        icon="mdi:sprout",
        name="Pigweed pollen concentration",
    ),
    SensorEntityDescription(
        key="pine",
        device_class="zadnego_ale__concentration",
        icon="mdi:pine-tree",
        name="Pine pollen concentration",
    ),
    SensorEntityDescription(
        key="plane_tree",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Plane Tree pollen concentration",
    ),
    SensorEntityDescription(
        key="plantain",
        device_class="zadnego_ale__concentration",
        icon="mdi:sprout",
        name="Plantain pollen concentration",
    ),
    SensorEntityDescription(
        key="poplar",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Poplar pollen concentration",
    ),
    SensorEntityDescription(
        key="ragweed",
        device_class="zadnego_ale__concentration",
        icon="mdi:sprout",
        name="Ragweed pollen concentration",
    ),
    SensorEntityDescription(
        key="sorrel",
        device_class="zadnego_ale__concentration",
        icon="mdi:sprout",
        name="Sorrel pollen concentration",
    ),
    SensorEntityDescription(
        key="willow",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Willow pollen concentration",
    ),
    SensorEntityDescription(
        key="yew",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Yew pollen concentration",
    ),
)

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
