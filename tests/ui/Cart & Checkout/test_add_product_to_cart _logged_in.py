import pytest
from pages.account_created_page import CreateAccountPage
from pages.brand_products_page import BrandProductPage
from pages.home_page import HomePage
from pages.login_home_page import LoginHomePage
from pages.product_details_page import ProductsDetailsPage
from pages.products_page import ProductsPage
from pages.signup_page import SignupPage
from pages.view_cart_page import ViewCartPage
from utils.assertions import assert_url, assert_verify_account_created, assert_text_match
from utils.test_data import generate_user_data


@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_add_product_to_cart_logged_in_1(page):
    home = HomePage(page)
    signup = SignupPage(page)
    createaccount = CreateAccountPage(page)
    loginhome = LoginHomePage(page)
    products = ProductsPage(page)
    brandproduct = BrandProductPage(page)
    productsdetails = ProductsDetailsPage(page)
    viewcart = ViewCartPage(page)

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
    await productsdetails.view_cart_click()

    await assert_text_match(await viewcart.get_product_tshirt(),"Men Tshirt","Product title")

    await assert_text_match(await viewcart.get_product_tshirt_price(),"Rs. 400","Product price")