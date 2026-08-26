from playwright.async_api import Page

from config import SiteConfig


class RostenderSite:
    def __init__(self, settings:SiteConfig):
        self.settings = settings

    async def search(self, page:Page):



# async def html_rostender(page, config):
#     await fill_and_search(page, "#keywords", config.search)
#     if config.exception_serch is not None:
#         await fill_and_search(page, "#exceptions", config.exception_serch)

#     await press_button(page, "#start-search-button")

#     current_url = page.url
#     html = await get_html(page)
#     pagi = await get_pagination_max_counter(html)
#     await pagination(page, current_url, pagi)