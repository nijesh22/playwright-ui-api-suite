import pytest
from pages.login_home_page import LoginHomePage
from pages.product_details_page import ProductsDetailsPage
from pages.products_page import ProductsPage
from utils.assertions import assert_equal_titles

@pytest.mark.parametrize("page", ["chromium"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
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
async def test_search_product_with_valid_keyword_1(page,search_name):

    loginhome = LoginHomePage(page)
    products = ProductsPage(page)
    product_details = ProductsDetailsPage(page)

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



