import pytest
from pages.brand_products_page import BrandProductPage
from pages.login_home_page import LoginHomePage
from pages.products_page import ProductsPage
from utils.assertions import assert_url

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_view_product_by_brand_1(page):
    loginhome = LoginHomePage(page)
    products = ProductsPage(page)
    brandproduct = BrandProductPage(page)

    await loginhome.menu_products_click()
    await products.click_brand_h3m()

    await assert_url(page, "https://automationexercise.com/brand_products/H&M")

    await brandproduct.click_brand_h3m_tshirt()

    await assert_url(page, "https://automationexercise.com/product_details/2")

