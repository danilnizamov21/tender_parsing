from playwright.async_api import Page

from browser.actions import click, fill
from config import SiteConfig


class SiteBidzaar:
    def __init__(self, settings: SiteConfig):
        self.settings = settings

    async def search(self, page: Page):
        """Поиск внутри сайта по ключевым словам с возможностью добавление слов исключений"""
        await fill(page, self.settings.search_input, self.settings.search)
        if self.settings.exception_serch is not None:
            await fill(page, self.settings.exlude_input, self.settings.exception_serch)

        await click(page, self.settings.search_button)
