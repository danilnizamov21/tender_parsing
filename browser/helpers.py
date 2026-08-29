from browser.actions import click, fill
from config import SiteConfig


async def search(page, settings: SiteConfig):
    """Поиск внутри сайта по ключевым словам с возможностью добавление слов исключений"""
    await fill(page, settings.search_input, settings.search)
    if settings.exception_serch is not None:
        await fill(page, settings.exlude_input, settings.exception_serch)

    await click(page, settings.search_button)


async def parse():
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
