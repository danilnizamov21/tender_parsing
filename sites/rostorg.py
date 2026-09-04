from playwright.async_api import Page

from browser.helpers import parse, search
from domain.models import Tender


class RostorgSite:
    def __init__(self, settings):
        self.settings = settings

    async def page_search(self, page: Page):
        return search(page, self.settings)

    async def urls(self, url: str, html: str) -> list[str]:

        return False

    async def page_parse(self, html: str) -> list[Tender]:
        return await parse(html, self.settings)
