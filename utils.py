async def press_button(page, button_name: str):
    await page.locator(button_name).click()
    await page.wait_for_timeout(10000)


async def fill_and_search(page, input_name: str, fill_str: str):

    await page.locator(input_name).first.fill(fill_str)
    await page.keyboard.press("Enter")
    await page.wait_for_timeout(10000)


async def get_html(page, name_file: str):
    html = await page.content()
    with open(f"{name_file}.html", "w") as f:
        f.write(html)
