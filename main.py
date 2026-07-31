import asyncio

from playwright.async_api import async_playwright


async def press_button(page, button_name: str):
    await page.locator(button_name).click()


async def fill_and_search(page, input_name: str, fill_str: str):

    await page.locator(input_name).first.fill(fill_str)
    await page.keyboard.press("Enter")

    await page.wait_for_timeout(1000)


async def get_html(page, name_file: str):
    html = await page.content()
    with open(f"{name_file}.html", "w") as f:
        f.write(html)


async def main(
    url: str, input_name: str, fill_str: str, filename: str, button_name: str
):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        await fill_and_search(page, input_name, fill_str)
        await press_button(page, button_name)
        await page.wait_for_timeout(10000)
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
