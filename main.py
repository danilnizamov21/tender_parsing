import asyncio

from playwright.async_api import async_playwright

from config import ROSTENDER, SiteConfig


async def main(config: SiteConfig):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(config.url)

        await config.prepare(page, config)
        await browser.close()


# sites = [ROSTENDER, BIDZAAR, B2B, ROSTORG]
# for site in sites:
asyncio.run(main(ROSTENDER))
