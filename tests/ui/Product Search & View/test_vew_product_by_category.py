import pytest
from utils.assertions import assert_url

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_vew_product_by_category_1(page,loginhome,products,categoryproduct):

    await loginhome.menu_products_click()
    await products.click_category_men()
    await products.click_category_men_tshirt()

    await assert_url(page, "https://automationexercise.com/category_products/3")

    await categoryproduct.mens_tshirt_click()

    await assert_url(page, "https://automationexercise.com/product_details/2")