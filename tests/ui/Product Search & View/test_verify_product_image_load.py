import pytest
from pages.login_home_page import LoginHomePage
from pages.products_page import ProductsPage
from utils.assertions import assert_image_is_loaded

@pytest.mark.parametrize("page", ["chromium"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_verify_product_image_load_1(page):
    loginhome = LoginHomePage(page)
    products = ProductsPage(page)

    await loginhome.menu_products_click()

    images = await products.get_product_images()

    for img in images:

        await assert_image_is_loaded(img, label="Product image")

