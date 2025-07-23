import lorem
import pytest
import random
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
async def test_submit_product_review_valid_1(page):
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
    await productsdetails.review_gmail_fill(f"rajuplaywright{random.randint(1000, 9999)}@test.com")
    await productsdetails.review_box_fill(lorem.sentence())

    await productsdetails.review_button_click()

    expected_validation = "Thank you for your review."
    actual_validation = await productsdetails.get_thank_you_alert_text()
    assert actual_validation == expected_validation, " 'Thank You' validation message is incorrect."
    print(" 'Thank You' message displayed successfully.")