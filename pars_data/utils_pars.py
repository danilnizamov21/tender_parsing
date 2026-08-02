from bs4 import BeautifulSoup

# with open("page.html", encoding="utf-8") as f:
#     html = f.read()


async def create_xml(html):
    soup = BeautifulSoup(html, "lxml")
    return soup


# articles = soup.find_all("article")

# for article in articles:
#     print("==============")
#     find_tag_a = article.a  # получение тега в котором хранится вся инфа
#     tit = find_tag_a["title"]  # получение тега внутри родительского для получения инфы
#     hrf = find_tag_a["href"]  # то же самое но только ищем ссылки
#     title = article.find(
#         "div", class_="starting-price__price starting-price--price"
#     )  # достаем блок в котором хранится цена
#     title2 = title.get_text()  # из блока достаем текст

#     print(f"{tit} \n https://rostender.info{hrf} \n {title2}")
#     # print(article)
#     i += 1
# print(i)


async def get_parent_tag(soup, tag: str):
    parents = soup.find_all(tag)
    return parents


async def get_tag_a(parent):
    tag_a = parent.a
    return tag_a


async def get_tag_div(parent, class_name):
    div = parent.find("div", class_=class_name)

    return div


async def get_href_from_a(tag_a):
    href = tag_a["href"]
    return href


async def get_title_from_a(tag_a):
    title = tag_a["title"]
    return title
