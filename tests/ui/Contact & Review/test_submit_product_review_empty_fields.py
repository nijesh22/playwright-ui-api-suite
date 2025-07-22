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
from utils.test_data import generate_user_data


@pytest.mark.parametrize("page", ["chromium"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_submit_product_review_empty_fields_1(page):
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
    productsdetails = ProductsDetailsPage(page)

    user = generate_user_data()

    name = "raju"
    email_address = ""
    comment = ""

    await home.go_to_signup_page()
    await signup.signup(user)

    await createaccount.continue_button_click()

    await loginhome.menu_products_click()
    await products.click_brand_h3m()

    await brandproduct.click_brand_h3m_tshirt()

    await productsdetails.review_name_fill(name)
    await productsdetails.review_gmail_fill(email_address)
    await productsdetails.review_box_fill(comment)

    await productsdetails.review_button_click()




