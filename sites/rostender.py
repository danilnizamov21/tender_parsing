from logging import config

from playwright.async_api import Page

from browser.actions import click, fill
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


async def max_page(html: str) -> int:
    """Получение максимального кол-во страниц для пагинации"""
    soup = await create_xml(html)
    parent = await get_parent_tag(soup, "div", "paginationWrapper")
    get_input_tag = await get_tag(parent, "input", "form-control")
    max_counter = get_input_tag.get("max")

    return max_counter


async def parse(html: str) -> list[Tender]:
    data = []

    soup = create_xml(html)
    parents = await get_all_parent_tag(soup, "article")
    for parent in parents:
        a = await get_tag_a(parent)
        title = await get_title_from_a(a)
        href = await get_href_from_a(a)
        div = await get_tag(
            parent, "div", "starting-price__price starting-price--price"
        )
        span = await get_tag(parent, "span", "black")

        data.append(
            {
                "title": title,
                "href": href,
                "cost": div.get_text(),
                "day": span.get_text(),
            }
        )

    return data


class RostenderSite:
    def __init__(self, settings: SiteConfig):
        self.settings = settings

    async def search(self, page: Page):
        """Поиск внутри сайта по ключевым словам с возможностью добавление слов исключений"""
        await fill(page, "#keywords", config.search)
        if config.exception_serch is not None:
            await fill(page, "#exceptions", config.exception_serch)

        await click(page, "#start-search-button")

    def urls(self, url: str, html: str) -> list[str]:
        """Созданиесписка URLов для пагинации"""
        pagi = max_page(html)
        urls = []
        for i in range(1, pagi + 1):
            urls.append(url + f"&page={i}")
        return urls

    def page_parse(html: str) -> list[Tender]:
        return parse(html)
