import pytest
from flows.brand_navigation_to_h3m_product_flow import go_to_brand_h3m_tshirt_and_assert_product
from utils.assertions import assert_verify_account_created
from utils.logger import Utils
from utils.test_data import generate_user_data

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_remove_product_from_cart(page,home,signup,viewcart,productsdetails,brandproduct,products,loginhome,createaccount,):
    user = generate_user_data()
    log = Utils.customlogger()

    await home.go_to_signup_page()
    await signup.signup(user)

    await assert_verify_account_created(page)

    await createaccount.continue_button_click()

    await loginhome.menu_products_click()

    await go_to_brand_h3m_tshirt_and_assert_product(page, products, brandproduct)

    await productsdetails.add_to_cart_click()
    await productsdetails.view_cart_click()

    await viewcart.click_cancel_cart_iteam()

    assert await viewcart.get_cart_is_empty_text() == "Cart is empty!", " Cart is not empty as expected."
    log.info(" Verified: Cart is empty.")
