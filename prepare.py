from config import SiteConfig
from utils import fill_and_search, get_html, press_button


async def prepare_rostender(page, config: SiteConfig):
    await fill_and_search(page, "#keywords", config.search)
    if config.exception_serch is not None:
        await fill_and_search(page, "#exceptions", config.exception_serch)
    await press_button(page, "#start-search-button")
    await get_html(page, config.output_filename)


async def prepare_bidzaar(page, config: SiteConfig):
    await fill_and_search(page, "#mat-input-bidzaar0", config.search)
    await get_html(page, config.output_filename)


async def prepare_b2b(page, config: SiteConfig):
    await fill_and_search(page, "#f_keyword", config.search)
    get_html(page, config.output_filename)


async def prepare_rostorg(page, config: SiteConfig):
    await fill_and_search(page, "input[name='query_field']")
