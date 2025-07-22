from pathlib import Path
import lorem
import pytest
import random
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
from utils.assertions import assert_url
from utils.test_data import generate_user_data


@pytest.mark.parametrize("page", ["chromium"], indirect=True)
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

    assert await page.locator("//b[normalize-space()='Account Created!']").is_visible()
    print("Account successfully created")

    await createaccount.continue_button_click()

    await loginhome.menu_products_click()
    await products.click_brand_h3m()

    expected_url = "https://automationexercise.com/brand_products/H&M"
    actual_url = page.url
    await assert_url(actual_url, expected_url)

    await brandproduct.click_brand_h3m_tshirt()

    expected_url1 = "https://automationexercise.com/product_details/2"
    actual_url1 = page.url
    await assert_url(actual_url1, expected_url1)

    await productsdetails.add_to_cart_click()

    await page.go_back()

    await brandproduct.click_brand_h3m_tshirt()

    await productsdetails.add_to_cart_click()

    await productsdetails.view_cart_click()

    await viewcart.proceed_to_checkout_click()

    await checkout.click_place_order()

    expected_url = "https://automationexercise.com/payment"
    actual_url = page.url
    await assert_url(actual_url, expected_url)

    await payement.fill_name_on_card("ram raj")
    await payement.fill_card_number("1234 1234 1234 1234")
    await payement.fill_cvc("123")
    await payement.fill_expiration("01")
    await payement.year_fill("2045")

    await payement.pay_and_order()

    payment_title = await payementdone.get_order_placed_title()


    assert payment_title == "Order Placed!" , "couldn't find the title"
    print("Successfully Verified Order Completion")

    await payementdone.click_download_invoice()

    download_path = Path("downloads")
    download_path.mkdir(parents=True, exist_ok=True)

    async with page.expect_download() as download_info:
        await page.click("text=Download")

    download = await download_info.value

    save_path = download_path / download.suggested_filename
    await download.save_as(save_path)

    assert save_path.exists(), f"Download failed: {save_path.name} not found."
    print(f"✅ File downloaded successfully: {save_path}")