import asyncio

from playwright.async_api import async_playwright

from config import BIDZAAR
from runner import SiteRunner
from sites.bidzaar import BidzaarSite


async def browser(config):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        site = BidzaarSite(config)
        runner = SiteRunner()
        await runner.run(site, page)

        await browser.close()


async def main():

    await browser(BIDZAAR)


if __name__ == "__main__":
    asyncio.run(main())
