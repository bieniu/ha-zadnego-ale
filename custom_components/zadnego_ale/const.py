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
        name="Alder Pollen Concentration",
    ),
    SensorEntityDescription(
        key="alternaria",
        device_class="zadnego_ale__concentration",
        icon="mdi:mushroom-outline",
        name="Alternaria Pollen Concentration",
    ),
    SensorEntityDescription(
        key="ash_tree",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Ash Tree Pollen Concentration",
    ),
    SensorEntityDescription(
        key="beech",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Beech Pollen Concentration",
    ),
    SensorEntityDescription(
        key="birch_tree",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Birch Tree Pollen Concentration",
    ),
    SensorEntityDescription(
        key="cladosporium",
        device_class="zadnego_ale__concentration",
        icon="mdi:mushroom-outline",
        name="Cladosporium Pollen Concentration",
    ),
    SensorEntityDescription(
        key="elm",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Elm Pollen Concentration",
    ),
    SensorEntityDescription(
        key="goldenrod",
        device_class="zadnego_ale__concentration",
        icon="mdi:grass",
        name="Goldenrod Pollen Concentration",
    ),
    SensorEntityDescription(
        key="grass",
        device_class="zadnego_ale__concentration",
        icon="mdi:grass",
        name="Grass Pollen Concentration",
    ),
    SensorEntityDescription(
        key="hazel",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Hazel Pollen Concentration",
    ),
    SensorEntityDescription(
        key="hornbeam",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Hornbeam Pollen Concentration",
    ),
    SensorEntityDescription(
        key="maple",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Maple Pollen Concentration",
    ),
    SensorEntityDescription(
        key="mugwort",
        device_class="zadnego_ale__concentration",
        icon="mdi:sprout",
        name="Mugwort Pollen Concentration",
    ),
    SensorEntityDescription(
        key="nettle",
        device_class="zadnego_ale__concentration",
        icon="mdi:sprout",
        name="Nettle Pollen Concentration",
    ),
    SensorEntityDescription(
        key="oak",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Oak Pollen Concentration",
    ),
    SensorEntityDescription(
        key="pigweed",
        device_class="zadnego_ale__concentration",
        icon="mdi:sprout",
        name="Pigweed Pollen Concentration",
    ),
    SensorEntityDescription(
        key="pine",
        device_class="zadnego_ale__concentration",
        icon="mdi:pine-tree",
        name="Pine Pollen Concentration",
    ),
    SensorEntityDescription(
        key="plane_tree",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Plane Tree Pollen Concentration",
    ),
    SensorEntityDescription(
        key="plantain",
        device_class="zadnego_ale__concentration",
        icon="mdi:sprout",
        name="Plantain Pollen Concentration",
    ),
    SensorEntityDescription(
        key="poplar",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Poplar Pollen Concentration",
    ),
    SensorEntityDescription(
        key="ragweed",
        device_class="zadnego_ale__concentration",
        icon="mdi:sprout",
        name="Ragweed Pollen Concentration",
    ),
    SensorEntityDescription(
        key="sorrel",
        device_class="zadnego_ale__concentration",
        icon="mdi:sprout",
        name="Sorrel Pollen Concentration",
    ),
    SensorEntityDescription(
        key="willow",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Willow Pollen Concentration",
    ),
    SensorEntityDescription(
        key="yew",
        device_class="zadnego_ale__concentration",
        icon="mdi:tree",
        name="Yew Pollen Concentration",
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
