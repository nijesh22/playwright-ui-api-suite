import pytest
from utils.logger import Utils

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_search_product_with_invalid_keyword_1(page,loginhome,products):
    log = Utils.customlogger()
    await loginhome.menu_products_click()

    await products.search_product("test")

    await products.search_button_click()

    product_elements = await products.products_all()
    assert len(product_elements) == 0, "Invalid keyword still shows products"
    log.info(" No products found — search with invalid keyword is working fine!")