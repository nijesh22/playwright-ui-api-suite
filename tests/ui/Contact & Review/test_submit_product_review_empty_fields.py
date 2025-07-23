import pytest
from pages.account_created_page import CreateAccountPage
from pages.brand_products_page import BrandProductPage
from pages.home_page import HomePage
from pages.login_home_page import LoginHomePage
from pages.product_details_page import ProductsDetailsPage
from pages.products_page import ProductsPage
from pages.signup_page import SignupPage
from utils.test_data import generate_user_data

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
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

    user = generate_user_data()

    await home.go_to_signup_page()
    await signup.signup(user)

    await createaccount.continue_button_click()

    await loginhome.menu_products_click()
    await products.click_brand_h3m()

    await brandproduct.click_brand_h3m_tshirt()

    await productsdetails.review_name_fill("raju")
    await productsdetails.review_gmail_fill("")
    await productsdetails.review_box_fill("")

    await productsdetails.review_button_click()




