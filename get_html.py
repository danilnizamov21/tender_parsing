from pars_html_data.prepare_pars import (
    get_pagination_max_counter,
    prepare_pars_b2b,
    prepare_pars_bidzaar,
    prepare_pars_rostender,
    prepare_pars_rostorg,
    save_to_excel,
)
from utils import fill_and_search, get_html, press_button


async def pagination(page, url: str, pagi_counter: int):
    c = 0
    while c != pagi_counter:
        c += 1
        new_url = url + f"&page={c}"
        await page.goto(new_url)
        html = await get_html(page)
        data = await prepare_pars_rostender(html)
        save_to_excel(data)
        await page.wait_for_timeout(5000)


async def html_rostender(page, config):
    await fill_and_search(page, "#keywords", config.search)
    if config.exception_serch is not None:
        await fill_and_search(page, "#exceptions", config.exception_serch)

    await press_button(page, "#start-search-button")

    current_url = page.url
    html = await get_html(page)
    pagi = await get_pagination_max_counter(html)
    await retrieving_html(page, current_url, pagi)


async def html_bidzaar(page, config):
    await fill_and_search(page, "#mat-input-bidzaar0", config.search)
    html = await get_html(page)
    await prepare_pars_bidzaar(html)


async def html_b2b(page, config):
    await fill_and_search(page, "#f_keyword", config.search)
    html = await get_html(page)
    await prepare_pars_b2b(html)


async def html_rostorg(page, config):
    await fill_and_search(page, "input[name='query_field']", config.search)
    html = await get_html(page)
    await prepare_pars_rostorg(html)
