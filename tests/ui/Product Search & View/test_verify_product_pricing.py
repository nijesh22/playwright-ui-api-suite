import pytest
from utils.assertions import assert_equal_prices

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_verify_product_pricing_1(page,loginhome,products,productsdetails):

    await loginhome.menu_products_click()

    product_elements = await products.products_all()
    product_count = len(product_elements)

    for i in range(product_count):
        product_price = await products.get_product_price_element_by_index(i)
        await products.click_product_view_buttons_index(i)

        product_details_price_name = await productsdetails.get_product_details_price_element()

        await assert_equal_prices(product_price, product_details_price_name)
        await page.go_back()