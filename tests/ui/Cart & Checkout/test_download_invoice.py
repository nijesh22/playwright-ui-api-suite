from pathlib import Path
import pytest
from pages.account_created_page import CreateAccountPage
from pages.brand_products_page import BrandProductPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_home_page import LoginHomePage
from pages.payement_page import PayementPage
from pages.payment_done_page import PayementDonePage
from pages.product_details_page import ProductsDetailsPage
from pages.products_page import ProductsPage
from pages.signup_page import SignupPage
from pages.view_cart_page import ViewCartPage
from utils.assertions import assert_url, assert_verify_account_created
from utils.downloads import download_and_verify
from utils.test_data import generate_user_data


@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_download_invoice_1(page):
    home = HomePage(page)
    signup = SignupPage(page)
    createaccount = CreateAccountPage(page)
    loginhome = LoginHomePage(page)
    products = ProductsPage(page)
    brandproduct = BrandProductPage(page)
    productsdetails = ProductsDetailsPage(page)
    viewcart = ViewCartPage(page)
    checkout = CheckoutPage(page)
    payement = PayementPage(page)
    payementdone = PayementDonePage(page)

    user = generate_user_data()

    await home.go_to_signup_page()
    await signup.signup(user)

    await assert_verify_account_created(page)

    await createaccount.continue_button_click()

    await loginhome.menu_products_click()
    await products.click_brand_h3m()

    await assert_url(page, "https://automationexercise.com/brand_products/H&M")

    await brandproduct.click_brand_h3m_tshirt()

    await assert_url(page, "https://automationexercise.com/product_details/2")

    await productsdetails.add_to_cart_click()

    await page.go_back()

    await brandproduct.click_brand_h3m_tshirt()

    await productsdetails.add_to_cart_click()

    await productsdetails.view_cart_click()

    await viewcart.proceed_to_checkout_click()

    await checkout.click_place_order()

    await assert_url(page, "https://automationexercise.com/payment")

    await payement.fill_card_details("ram raj","1234 1234 1234 1234","123","01","2045")

    await payement.pay_and_order()

    payment_title = await payementdone.get_order_placed_title()

    assert payment_title == "Order Placed!" , "couldn't find the title"
    print("Successfully Verified Order Completion")

    await payementdone.click_download_invoice()

    await download_and_verify(page, locator="text=Download")
