"""Constants for Zadnego Ale integration."""
from datetime import timedelta

ATTRIBUTION = (
    "Dane dostarczone przez Ośrodek Badania Alergenów Środowiskowych Sp. z o.o."
)

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
    "alternaria": ("mdi:mushroom-outline"),
    "ambrozja": ("mdi:sprout"),
    "babka": ("mdi:sprout"),
    "brzoza": ("mdi:tree"),
    "bylica": ("mdi:sprout"),
    "cis": ("mdi:tree"),
    "cladosporium": ("mdi:mushroom-outline"),
    "dąb": ("mdi:tree"),
    "jesion": ("mdi:tree"),
    "komosa": ("mdi:sprout"),
    "leszczyna": ("mdi:tree"),
    "olsza": ("mdi:tree"),
    "pokrzywa": ("mdi:sprout"),
    "szczaw": ("mdi:sprout"),
    "topola": ("mdi:tree"),
    "trawy": ("mdi:grass"),
    "wierzba": ("mdi:tree"),
    "wiąz": ("mdi:tree"),
}
