import re
import pytest
from pages.brand_products_page import BrandProductPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_home_page import LoginHomePage
from pages.product_details_page import ProductsDetailsPage
from pages.products_page import ProductsPage
from pages.signup_page import SignupPage
from pages.view_cart_page import ViewCartPage
from utils.assertions import assert_url

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_verify_address_details_during_checkout_1(page):
    home = HomePage(page)
    signup = SignupPage(page)
    loginhome = LoginHomePage(page)
    products = ProductsPage(page)
    brandproduct = BrandProductPage(page)
    productsdetails = ProductsDetailsPage(page)
    viewcart = ViewCartPage(page)
    check_out = CheckoutPage(page)

    await home.go_to_signup_page()
    await signup.login("nijesh@gmail.com","qwerty@123")
    await assert_url(page,"https://automationexercise.com/")

    await loginhome.menu_products_click()
    await products.click_brand_h3m()

    await assert_url(page, "https://automationexercise.com/brand_products/H&M")

    await brandproduct.click_brand_h3m_tshirt()

    await assert_url(page, "https://automationexercise.com/product_details/2")

    await productsdetails.add_to_cart_click()
    await productsdetails.view_cart_click()
    await viewcart.proceed_to_checkout_click()

    await assert_url(page, "https://automationexercise.com/checkout")

    actual_delivery_address = await check_out.get_delivery_address()

    # Normalize: remove newlines, tabs, and extra spaces
    actual_clean = re.sub(r'\s+', ' ', actual_delivery_address).strip()

    excepted_address = "Your delivery address Mr. nijesh mannuel Street address, P.O. Box, Company name ernakulam kerala 682001 India 1231231231"

    assert actual_clean == excepted_address, f"❌ Address mismatch:\nExpected: {excepted_address}\nGot: {actual_clean}"
    print("✅ Delivery address verified successfully!")


