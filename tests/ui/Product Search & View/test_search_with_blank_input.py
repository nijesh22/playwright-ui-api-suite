import pytest
from pages.login_home_page import LoginHomePage
from pages.products_page import ProductsPage
from utils.assertions import assert_url

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_search_with_blank_input_1(page):

    loginhome = LoginHomePage(page)
    products = ProductsPage(page)

    await loginhome.menu_products_click()
    await products.search_product("")
    await products.search_button_click()

    await assert_url(page,"https://automationexercise.com/products?search=")
