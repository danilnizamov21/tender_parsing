from bs4 import BeautifulSoup


async def create_xml(html):
    soup = BeautifulSoup(html, "lxml")
    return soup


async def get_parent_tag(soup, tag: str, class_name=None):
    """Получение родительского тега"""
    if class_name is None:
        parents = soup.find_all(tag)
    else:
        parents = soup.find_all(tag, class_=class_name)
    return parents


async def get_tag_a(parent):
    """Получение тега <a>.Для получения требуятся тэг родитель"""
    tag_a = parent.a
    return tag_a


async def get_tag(parent, tag, class_name: str):
    """Получение любого тега внутри родительского класса"""
    div = parent.find(tag, class_=class_name)

    return div


async def get_href_from_a(tag_a) -> str | None:
    """Получение ссылки из тега <a>"""
    href = tag_a["href"]
    return href


async def get_title_from_a(tag_a) -> str | None:
    """Получение описания внутри тега <a>"""
    title = tag_a["title"]
    return title

async def get_pagination_counter(parent):
    