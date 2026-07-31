from collections.abc import Callable
from dataclasses import dataclass

from prepare import prepare_b2b, prepare_bidzaar, prepare_rostender, prepare_rostorg


@dataclass
class SiteConfig:
    url: str
    search: str
    exception_serch: str | None
    output_filename: str
    prepare: Callable


ROSTENDER = SiteConfig(
    "https://rostender.info/extsearch/advanced",
    "Видеосъемка",
    "поставка",
    "rostender",
    prepare_rostender,
)

BIDZAAR = SiteConfig(
    "https://bidzaar.com/app/requests/public/buy",
    "Видеосъемка",
    None,
    "bidzaar",
    prepare_bidzaar,
)

B2B = SiteConfig(
    "https://www.b2b-center.ru/market/", "Видеосъемка", None, "b2b", prepare_b2b
)

ROSTORG = SiteConfig(
    "https://www.roseltorg.ru/procedures/search",
    "Видеосъемка",
    None,
    "rostorg",
    prepare_rostorg,
)
