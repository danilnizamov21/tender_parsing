from pars_html_data.prepare_pars import (
    get_pagination_max_counter,
    prepare_pars_b2b,
    prepare_pars_bidzaar,
    prepare_pars_rostender,
    prepare_pars_rostorg,
)
from utils import fill_and_search, get_html, press_button


async def retrieving_html(page, url: str, pagi_counter: int, c: int):
    c = 0
    while c != pagi_counter:
        c += 1
        url = url + f"&{c}"
        html = await get_html(page)
        await prepare_pars_rostender(html)


async def prepare_rostender(page, config):
    await fill_and_search(page, "#keywords", config.search)
    if config.exception_serch is not None:
        await fill_and_search(page, "#exceptions", config.exception_serch)
    await press_button(page, "#start-search-button")
    current_url = page.url
    html = await get_html(page)
    pagi = await get_pagination_max_counter(html)
    await prepare_pars_rostender(html)

    # await prepare_pars_rostender(html)
    url = page.url
    print(f"CURRENT URL IS  ====== {url}")


async def prepare_bidzaar(page, config):
    await fill_and_search(page, "#mat-input-bidzaar0", config.search)
    html = await get_html(page)
    await prepare_pars_bidzaar(html)


async def prepare_b2b(page, config):
    await fill_and_search(page, "#f_keyword", config.search)
    html = await get_html(page)
    await prepare_pars_b2b(html)


async def prepare_rostorg(page, config):
    await fill_and_search(page, "input[name='query_field']", config.search)
    html = await get_html(page)
    await prepare_pars_rostorg(html)
