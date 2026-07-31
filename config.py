from collections.abc import Callable
from dataclasses import dataclass

from prepare import prepare_rostender


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
