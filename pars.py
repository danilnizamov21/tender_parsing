from bs4 import BeautifulSoup

with open("page.html", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")
i = 0
articles = soup.find_all("article")
for article in articles:
    print("==============")
    find_tag_a = article.a
    tit = find_tag_a["title"]
    hrf = find_tag_a["href"]
    title = article.find("div", class_="starting-price__price starting-price--price")
    title2 = title.get_text()
    print(f"{tit} \n https://rostender.info{hrf} \n {title2}")
    # print(article)
    i += 1
print(i)
