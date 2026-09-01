from playwright.async_api import Page

from browser.helpers import search
from config import SiteConfig
from domain.models import Tender
from pars_html_data.utils_pars import (
    create_xml,
    get_all_parent_tag,
    get_href_from_a,
    get_parent_tag,
    get_tag,
    get_tag_a,
    get_title_from_a,
)


def max_page(html: str) -> int:
    """Получение максимального кол-во страниц для пагинации"""
    soup = create_xml(html)
    parent = get_parent_tag(soup, "div", "paginationWrapper")
    get_input_tag = get_tag(parent, "input", "form-control")
    max_counter = get_input_tag.get("max")

    return max_counter


def _parse(html: str) -> list[Tender]:
    data = []

    soup = create_xml(html)
    parents = get_all_parent_tag(soup, "article")
    for parent in parents:
        a = get_tag_a(parent)
        title = get_title_from_a(a)
        href = get_href_from_a(a)
        div = get_tag(parent, "div", "starting-price__price starting-price--price")
        span = get_tag(parent, "span", "black")

        data.append(
            Tender(
                source="rostender",
                title=title or "",
                url=f"https://rostender.info{href}" or "",
                price=div.get_text(strip=True) if div else None,
                deadline=span.get_text(strip=True) if span else None,
            )
        )

    return data


class RostenderSite:
    def __init__(self, settings: SiteConfig):
        self.settings = settings

    async def page_search(self, page: Page):
        """Поиск внутри сайта по ключевым словам с возможностью добавление слов исключений"""
        return await search(page, self.settings)

    async def urls(self, url: str, html: str) -> list[str]:
        """Созданиесписка URLов для пагинации"""
        pagi = int(max_page(html))
        urls = []
        for i in range(1, pagi + 1):
            urls.append(url + f"&page={i}")
        return urls

    async def page_parse(self, html: str) -> list[Tender]:
        return _parse(html)
