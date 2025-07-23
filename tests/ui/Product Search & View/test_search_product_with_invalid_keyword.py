import pytest
from pages.login_home_page import LoginHomePage
from pages.products_page import ProductsPage

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_search_product_with_invalid_keyword_1(page):

    loginhome = LoginHomePage(page)
    products = ProductsPage(page)

    await loginhome.menu_products_click()

    await products.search_product("test")

    await products.search_button_click()

    product_elements = await products.products_all()
    assert len(product_elements) == 0, "Invalid keyword still shows products"
    print("✅ No products found — search with invalid keyword is working fine!")