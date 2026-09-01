from dataclasses import dataclass


@dataclass
class SiteConfig:
    url: str
    search: str
    exception_serch: str | None
    output_filename: str
    search_input: str
    exlude_input: str | None
    search_button: str | None
    parents_tag: str | None
    title_tag: str | None
    title_classname: str | None
    day_tag: str | None
    day_classname: str | None


ROSTENDER = SiteConfig(
    "https://rostender.info/extsearch/advanced",
    "Видеосъемка",
    "поставка",
    "rostender",
    "#keywords",
    "#exceptions",
    "#start-search-button",
    None,
    None,
    None,
    None,
    None,
)

# BIDZAAR = SiteConfig(
#     "https://bidzaar.com/app/requests/public/buy",
#     "Видеосъемка",
#     None,
#     "bidzaar",
#     bidzaar,
# )

# B2B = SiteConfig("https://www.b2b-center.ru/market/", "трубы", None, "b2b", html_b2b)

# ROSTORG = SiteConfig(
#     "https://www.roseltorg.ru/procedures/search",
#     "Видеосъемка",
#     None,
#     "rostorg",
#     html_rostorg,
# )
