import re
import pytest
from flows.brand_navigation_to_h3m_product_flow import go_to_brand_h3m_tshirt_and_assert_product
from utils.assertions import assert_url
from utils.logger import Utils


@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_verify_address_details_during_checkout_1(page,brandproduct,products,checkout,home,signup,loginhome,productsdetails,viewcart):
    log = Utils.customlogger()

    await home.go_to_signup_page()
    await signup.login("nijesh@gmail.com","qwerty@123")
    await assert_url(page,"https://automationexercise.com/")

    await loginhome.menu_products_click()

    await go_to_brand_h3m_tshirt_and_assert_product(page, products, brandproduct)

    await productsdetails.add_to_cart_click()
    await productsdetails.view_cart_click()
    await viewcart.proceed_to_checkout_click()

    await assert_url(page, "https://automationexercise.com/checkout")

    actual_delivery_address = await checkout.get_delivery_address()

    # Normalize: remove newlines, tabs, and extra spaces
    actual_clean = re.sub(r'\s+', ' ', actual_delivery_address).strip()

    excepted_address = "Your delivery address Mr. nijesh mannuel Street address, P.O. Box, Company name ernakulam kerala 682001 India 1231231231"

    assert actual_clean == excepted_address, f"❌ Address mismatch:\nExpected: {excepted_address}\nGot: {actual_clean}"
    log.info("✅ Delivery address verified successfully!")


