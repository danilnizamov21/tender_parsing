from config import SiteConfig
from pars_data.prepare_pars import (
    prepare_pars_b2b,
    prepare_pars_bidzaar,
    prepare_pars_rostender,
    prepare_pars_rostorg,
)
from utils import fill_and_search, get_html, press_button


async def prepare_rostender(page, config: SiteConfig):
    await fill_and_search(page, "#keywords", config.search)
    if config.exception_serch is not None:
        await fill_and_search(page, "#exceptions", config.exception_serch)
    await press_button(page, "#start-search-button")
    html = await get_html(page)
    await prepare_pars_rostender(html)


async def prepare_bidzaar(page, config: SiteConfig):
    await fill_and_search(page, "#mat-input-bidzaar0", config.search)
    html = await get_html(page)
    await prepare_pars_bidzaar(html)


async def prepare_b2b(page, config: SiteConfig):
    await fill_and_search(page, "#f_keyword", config.search)
    html = await get_html(page)
    await prepare_pars_b2b(html)


async def prepare_rostorg(page, config: SiteConfig):
    await fill_and_search(page, "input[name='query_field']", config.search)
    html = await get_html(page)
    await prepare_pars_rostorg(html)
