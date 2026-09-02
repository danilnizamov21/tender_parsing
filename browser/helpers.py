from browser.actions import click, fill
from config import SiteConfig
from domain.models import Tender
from pars_html_data.utils_pars import (
    create_xml,
    get_all_parent_tag,
    get_href_from_a,
    get_tag,
    get_tag_a,
)


async def search(page, settings: SiteConfig):
    """Поиск внутри сайта по ключевым словам с возможностью добавление слов исключений"""
    await fill(page, settings.search_input, settings.search)
    if settings.exception_serch is not None:
        await fill(page, settings.exlude_input, settings.exception_serch)
    if settings.search_button is not None:
        await click(page, settings.search_button)


async def parse(html: str, settings: SiteConfig) -> list[Tender]:
    data = []
    soup = create_xml(html)
    parents = get_all_parent_tag(soup, settings.parents_tag)

    for parent in parents:
        a = get_tag_a(parent)
        print(a)
        href = get_href_from_a(a) if a else None
        if not href:
            continue
        title = get_tag(parent, settings.title_tag, settings.title_classname)
        day = get_tag(parent, settings.day_tag, settings.day_classname)
        data.append(
            Tender(
                source=settings.output_filename,
                title=title.get_text(strip=True) if title else None,
                url=href,
                price=None,
                deadline=day.get_text(strip=True) if day else None,
            )
        )

    return data
