import pytest
from flows.brand_navigation_to_h3m_product_flow import go_to_brand_h3m_tshirt_and_assert_product
from flows.register_flow import register_new_user_flow
from utils.assertions import assert_text_match
from utils.test_data import generate_user_data

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_add_product_to_cart_logged_in(page,home,signup,createaccount,loginhome,products,brandproduct,productsdetails,viewcart):

    user = generate_user_data()
    await register_new_user_flow(page, home, signup, createaccount, user)
    await loginhome.menu_products_click()
    await go_to_brand_h3m_tshirt_and_assert_product(page, products, brandproduct)
    await productsdetails.add_to_cart_click()
    await productsdetails.view_cart_click()
    await assert_text_match(await viewcart.get_product_tshirt(),"Men Tshirt","Product title")
    await assert_text_match(await viewcart.get_product_tshirt_price(),"Rs. 400","Product price")