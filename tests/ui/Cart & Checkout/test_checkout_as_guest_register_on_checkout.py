import pytest
from flows.brand_navigation_to_h3m_product_flow import go_to_brand_h3m_tshirt_and_assert_product
from flows.register_flow import register_new_user_flow
from utils.assertions import assert_url
from utils.test_data import generate_user_data

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_checkout_as_guest_register_on_checkout_1(page,home,createaccount,signup,viewcart,productsdetails,loginhome,products,brandproduct):

    await loginhome.menu_products_click()

    await go_to_brand_h3m_tshirt_and_assert_product(page, products, brandproduct)

    await productsdetails.add_to_cart_click()
    await productsdetails.view_cart_click()

    await viewcart.proceed_to_checkout_click()

    await viewcart.register_or_login_click()

    user = generate_user_data()

    await register_new_user_flow(page, home, signup, createaccount, user)

    await loginhome.menu_cart_click()

    await viewcart.proceed_to_checkout_click()

    await assert_url(page, "https://automationexercise.com/checkout")



