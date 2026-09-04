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
    cost_tag: str | None
    cost_classname: str | None


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
    None,
    None,
)

BIDZAAR = SiteConfig(
    url="https://bidzaar.com/app/requests/public/buy",
    search="трубы",
    exception_serch=None,
    output_filename="bidzaar",
    search_input="#mat-input-bidzaar0",
    exlude_input=None,
    search_button=None,
    parents_tag="li",
    title_tag="span",
    title_classname="name-item ui-name with-dot",
    day_tag="div",
    day_classname="date",
    cost_tag=None,
    cost_classname=None,
)

B2B = SiteConfig(
    url="https://www.b2b-center.ru/market/",
    search="трубы",
    exception_serch=None,
    output_filename="b2b",
    search_input="#f_keyword",
    exlude_input=None,
    search_button=None,
    parents_tag="tr",
    title_tag="div",
    title_classname="search-results-title-desc",
    day_tag="td",
    day_classname="nowrap",
    cost_tag=None,
    cost_classname=None,
)

# ROSTORG = SiteConfig(
#     url="https://www.roseltorg.ru/procedures/search",
#     search="Видеосъемка",
#     exception_serch=None,
#     output_filename="rostorg",
#     search_input=html_rostorg,
# )
