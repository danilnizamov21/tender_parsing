from collections.abc import Callable
from dataclasses import dataclass

from get_html import (
    html_b2b,
    html_bidzaar,
    html_rostender,
    html_rostorg,
)


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
    html_rostender,
)

BIDZAAR = SiteConfig(
    "https://bidzaar.com/app/requests/public/buy",
    "Видеосъемка",
    None,
    "bidzaar",
    html_bidzaar,
)

B2B = SiteConfig("https://www.b2b-center.ru/market/", "трубы", None, "b2b", html_b2b)

ROSTORG = SiteConfig(
    "https://www.roseltorg.ru/procedures/search",
    "Видеосъемка",
    None,
    "rostorg",
    html_rostorg,
)
