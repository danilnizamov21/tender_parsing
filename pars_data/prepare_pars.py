from pars_data.utils_pars import (
    create_xml,
    get_href_from_a,
    get_parent_tag,
    get_tag,
    get_tag_a,
    get_title_from_a,
)


async def prepare_pars_rostender(html):
    soup = await create_xml(html)
    parents = await get_parent_tag(soup, "article")
    for parent in parents:
        a = await get_tag_a(parent)
        title = await get_title_from_a(a)
        href = await get_href_from_a(a)
        div = await get_tag(
            parent, "div", "starting-price__price starting-price--price"
        )
        span = await get_tag(parent, "span", "black")
        print(
            f"title={title} \n href = {href} \n cost={div.get_text()} \n day={span.get_text()}"
        )


async def prepare_pars_b2b(html):
    soup = await create_xml(html)
    parents = await get_parent_tag(soup, "tr")
    for parent in parents:
        a = await get_tag_a(parent)
        href = await get_href_from_a(a)
        title = await get_tag(parent, "div", "search-results-title-desc")
        day = await get_tag(parent, "td", "nowrap")

        title_text = title.get_text(strip=True) if title else "N/A"
        day_text = day.get_text(strip=True) if day else "N/A"

        print(f"title={title_text} \n href = {href} \n cost= - \n day={day_text}")


async def prepare_pars_bidzaar(html):
    soup = await create_xml(html)
    parents = await get_parent_tag(soup, "li")
    for parent in parents:
        a = await get_tag_a(parent)
        href = await get_href_from_a(a)
        title = await get_tag(parent, "span", "name-item ui-name with-dot")
        day = await get_tag(parent, "div", "date")

        title_text = title.get_text(strip=True) if title else "N/A"
        day_text = day.get_text(strip=True) if day else "N/A"

        print(f"title={title_text} \n href = {href} \n cost= - \n day={day_text}")


async def prepare_pars_rostorg(html):
    soup = await create_xml(html)
    parents = await get_parent_tag(soup, "div", "search-results__item autoload-post")
    for parent in parents:
        a = await get_tag_a(parent)
        href = await get_href_from_a(a)
        title = await get_tag(
            parent, "a", "search-results__link search-results__link--description"
        )
        cost = await get_tag(parent, "p", "tablet")
        day = await get_tag(parent, "time", "search-results__time")

        title_text = title.get_text(strip=True) if title else "N/A"
        day_text = day.get_text(strip=True) if day else "N/A"
        cost_text = cost.get_text(strip=True) if cost else "N/A"

        print(
            f"title={title_text} \n href = {href} \n cost={cost_text} \n day={day_text}"
        )
