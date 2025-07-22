import pytest
from pages.brand_products_page import BrandProductPage
from pages.category_products_page import CategoryProductPage
from pages.login_home_page import LoginHomePage
from pages.products_page import ProductsPage
from utils.assertions import assert_url

@pytest.mark.parametrize("page", ["chromium"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_view_product_by_brand_1(page):

    loginhome = LoginHomePage(page)
    products = ProductsPage(page)
    categoryproduct = CategoryProductPage(page)
    brandproduct = BrandProductPage(page)

    await loginhome.menu_products_click()
    await products.click_brand_h3m()

    expected_url = "https://automationexercise.com/brand_products/H&M"
    actual_url = page.url
    await assert_url(actual_url, expected_url)

    await brandproduct.click_brand_h3m_tshirt()

    expected_url1 = "https://automationexercise.com/product_details/2"
    actual_url1 = page.url
    await assert_url(actual_url1, expected_url1)

