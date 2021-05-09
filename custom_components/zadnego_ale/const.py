"""Constants for Zadnego Ale integration."""
from __future__ import annotations

from datetime import timedelta
from typing import Final

ATTRIBUTION: Final = (
    "Dane dostarczone przez Ośrodek Badania Alergenów Środowiskowych Sp. z o.o."
)

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

SENSORS: Final[dict[str, str]] = {
    "alternaria": "mdi:mushroom-outline",
    "ambrozja": "mdi:sprout",
    "babka": "mdi:sprout",
    "brzoza": "mdi:tree",
    "buk": "mdi:tree",
    "bylica": "mdi:sprout",
    "cis": "mdi:tree",
    "cladosporium": "mdi:mushroom-outline",
    "dąb": "mdi:tree",
    "grab": "mdi:tree",
    "jesion": "mdi:tree",
    "klon": "mdi:tree",
    "komosa": "mdi:sprout",
    "leszczyna": "mdi:tree",
    "olsza": "mdi:tree",
    "platan": "mdi:tree",
    "pokrzywa": "mdi:sprout",
    "szczaw": "mdi:sprout",
    "topola": "mdi:tree",
    "trawy": "mdi:grass",
    "wierzba": "mdi:tree",
    "wiąz": "mdi:tree",
}
