from pars_data.utils_pars import (
    create_xml,
    get_href_from_a,
    get_parent_tag,
    get_tag_a,
    get_tag_div,
    get_title_from_a,
)


async def prepare_pars_rostender(html):
    soup = await create_xml(html)
    parents = await get_parent_tag(soup, "article")
    for parent in parents:
        a = await get_tag_a(parent)
        title = await get_title_from_a(a)
        href = await get_href_from_a(a)
        div = await get_tag_div(parent, "starting-price__price starting-price--price")

        print(f"title={title} \n href = {href} \n cost={div.get_text()}")
