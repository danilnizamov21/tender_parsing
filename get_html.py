# from utils import fill_and_search, get_html

# from pars_html_data.prepare_pars import (
#     prepare_pars_b2b,
#     prepare_pars_bidzaar,
# )


# async def html_bidzaar(page, config):
#     await fill_and_search(page, "#mat-input-bidzaar0", config.search)
#     html = await get_html(page)
#     await prepare_pars_bidzaar(html)


# async def html_b2b(page, config):
#     await fill_and_search(page, "#f_keyword", config.search)
#     html = await get_html(page)
#     await prepare_pars_b2b(html)


# async def html_rostorg(page, config):
#     await fill_and_search(page, "input[name='query_field']", config.search)
#     current_url = page.url

#     await pagination(page, current_url, 50)
