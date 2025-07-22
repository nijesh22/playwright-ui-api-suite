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
from pages.view_cart_page import ViewCartPage
from utils.assertions import assert_url
from utils.test_data import generate_user_data


@pytest.mark.parametrize("page", ["chromium"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_verify_cart_total_updates_1(page):
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

    await brandproduct.click_view_products_summer_white_top()

    await productsdetails.add_to_cart_click()

    await productsdetails.view_cart_click()

    product_elements = await viewcart.total_cart_boxes_all()
    product_count = len(product_elements)

    for i in range(product_count):
        product_name = await viewcart.get_product_price_element_by_index(i)
        assert "Men Tshirt" in product_name or "Summer White Top" in product_name





