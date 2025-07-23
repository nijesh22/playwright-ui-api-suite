
import pytest
from playwright.async_api import async_playwright

@pytest.fixture
async def page(request):
    browser_name = request.param  # passed via @pytest.mark.parametrize
    async with async_playwright() as p:
        browser = {
            "chromium": p.chromium,
            "firefox": p.firefox,
            "webkit": p.webkit  # WebKit covers Safari/Edge scenarios
        }[browser_name]

        browser_instance = await browser.launch(headless=False, slow_mo=500)
        page = await browser_instance.new_page()
        yield page
        await browser_instance.close()
