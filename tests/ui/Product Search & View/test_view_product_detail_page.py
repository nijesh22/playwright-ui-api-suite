import pytest
from utils.assertions import assert_equal_titles

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_view_product_detail_page_1(page,loginhome,products,productsdetails):
    await loginhome.menu_products_click()

    product_elements = await products.products_all()
    product_count = len(product_elements)

    for i in range(product_count):
        product_name = await products.get_product_element_by_index(i)
        await products.click_product_view_buttons_index(i)

        product_details_name = await productsdetails.get_product_details_element()

        await assert_equal_titles(product_name, product_details_name)
        await page.go_back()

        await products.search_product_clear()







