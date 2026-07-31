import asyncio

from playwright.async_api import async_playwright


# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto("https://rostender.info/")
# search = page.get_by_placeholder(
#     "Введите ключевые слова, например “ремонт дорог в Новосибирске”"
# )
# await search.fill("Видеосъемка")
# await search.press("Enter")
# await page.wait_for_load_state("networkidle")
# await page.locator("input[name='exceptions']").fill("поставка, оборудование")
# print(page.url)
# await page.wait_for_timeout(10000)
# await page.keyboard.press("Tab")
# await page.locator("#start-search-button").click()
# print(page.url)
# await page.wait_for_timeout(20000)
# html = await page.content()
# with open("page.html", "w") as f:
#     f.write(html)
# print(page.url)
# await browser.close()
async def press_button(page):
    await page.locator("#start-search-button").click()


async def fill_and_search(page, input_name: str, fill_str: str):

    await page.locator(input_name).first.fill(fill_str)
    await page.keyboard.press("Enter")

    await page.wait_for_timeout(1000)


async def get_html(page, name_file: str):
    html = await page.content()
    with open(f"{name_file}.html", "w") as f:
        f.write(html)


async def main(url: str, input_name: str, fill_str: str, filename: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        await fill_and_search(page, input_name, fill_str)
        await press_button(page)
        await page.wait_for_timeout(1000)
        await get_html(page, filename)


asyncio.run(
    main("https://rostender.info/extsearch/advanced", "#keywords", "видеосъемка", "1")
)
# asyncio.run(
#     main(
#         "https://www.b2b-center.ru/market/",
#         "#f_keyword",
#         "Видеосъемка",
#         "2",
#     )
# )
