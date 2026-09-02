import asyncio

from playwright.async_api import async_playwright

from config import B2B
from runner import SiteRunner
from sites.b2b import B2BSite


async def browser(config):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        site = B2BSite(config)
        runner = SiteRunner()
        await runner.run(site, page)

        await browser.close()


async def main():

    await browser(B2B)


if __name__ == "__main__":
    asyncio.run(main())
