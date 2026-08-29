from playwright.async_api import Page

from browser.helpers import search
from config import SiteConfig


class SiteBidzaar:
    def __init__(self, settings: SiteConfig):
        self.settings = settings

    async def page_search(self, page: Page):
        """Поиск внутри сайта по ключевым словам с возможностью добавление слов исключений"""
        return await search(page, self.settings)

    async def page_parse(self, html: str) -> list[Tender]:
        return parse(html)
