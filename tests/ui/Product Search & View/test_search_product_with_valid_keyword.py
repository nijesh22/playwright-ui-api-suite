import pytest
from utils.assertions import assert_equal_titles

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
@pytest.mark.parametrize("search_name", [
    "Blue Top",
    "Men Tshirt",
    "Sleeveless Dress",
    "Stylish Dress",
    "Winter Top",
    "Summer White Top",
    "Madame Top For Women",
    "Fancy Green Top"
])
async def test_search_product_with_valid_keyword(page,search_name,loginhome,products):

    await loginhome.menu_products_click()

    await products.search_product(search_name)

    search_text = await products.search_product_name_get(search_name)

    await products.search_button_click()

    # Get search result products
    search_result_elements = await products.get_product_element_singles()
    product_count = len(search_result_elements)

    for i in range(min(8, product_count)):
        product_name = await products.get_product_element_by_index_search(i)

        await assert_equal_titles(search_text, product_name)
        await page.go_back()



