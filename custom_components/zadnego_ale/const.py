"""Constants for Zadnego Ale integration."""
from datetime import timedelta

ATTR_ICON = "icon"

CONF_REGION = "region"

DEFAULT_NAME = "Żadnego Ale"
DEFAULT_UPDATE_INTERVAL = timedelta(minutes=60)
DOMAIN = "zadnego_ale"

REGIONS = (
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

SENSORS = {
    "alternaria": {ATTR_ICON: None},
    "ambrozja": {ATTR_ICON: None},
    "babka": {ATTR_ICON: None},
    "brzoza": {ATTR_ICON: None},
    "bylica": {ATTR_ICON: None},
    "cis": {ATTR_ICON: None},
    "cladosporium": {
        ATTR_ICON: "mdi:mushroom-outline",
    },
    "dąb": {ATTR_ICON: None},
    "komosa": {ATTR_ICON: None},
    "leszczyna": {ATTR_ICON: None},
    "olsza": {ATTR_ICON: None},
    "pokrzywa": {ATTR_ICON: None},
    "szczaw": {ATTR_ICON: None},
    "topola": {ATTR_ICON: None},
    "trawy": {ATTR_ICON: None},
    "wierzba": {ATTR_ICON: None},
    "wiąz": {ATTR_ICON: None},
}
