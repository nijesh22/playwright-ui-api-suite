import pytest

from flows.brand_navigation_to_h3m_product_flow import go_to_brand_h3m_tshirt_and_assert_product
from flows.register_flow import register_new_user_flow
from utils.test_data import generate_user_data

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_verify_cart_total_updates_1(page,home,viewcart,productsdetails,signup,createaccount,loginhome,products,brandproduct):

    user = generate_user_data()

    await register_new_user_flow(page, home, signup, createaccount, user)

    await loginhome.menu_products_click()

    await go_to_brand_h3m_tshirt_and_assert_product(page, products, brandproduct)

    await productsdetails.add_to_cart_click()

    await page.go_back()

    await brandproduct.click_view_products_summer_white_top()

    await productsdetails.add_to_cart_click()

    await productsdetails.view_cart_click()

    product_elements = await viewcart.total_cart_boxes_all()
    product_count = len(product_elements)

    for i in range(product_count):
        product_name = await viewcart.get_product_price_element_by_index(i)
        assert "Men Tshirt" in product_name or "Summer White Top" in product_name





