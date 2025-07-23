import pytest
from pages.account_created_page import CreateAccountPage
from pages.brand_products_page import BrandProductPage
from pages.home_page import HomePage
from pages.login_home_page import LoginHomePage
from pages.product_details_page import ProductsDetailsPage
from pages.products_page import ProductsPage
from pages.signup_page import SignupPage
from pages.view_cart_page import ViewCartPage
from utils.assertions import assert_url, assert_verify_account_created
from utils.test_data import generate_user_data


@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_attempt_to_access_profile_without_login_1(page):
    home = HomePage(page)
    signup = SignupPage(page)
    createaccount = CreateAccountPage(page)
    loginhome = LoginHomePage(page)
    products = ProductsPage(page)
    brandproduct = BrandProductPage(page)
    productsdetails = ProductsDetailsPage(page)
    viewcart = ViewCartPage(page)
    loginhomepage = LoginHomePage(page)

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

    await brandproduct.click_view_products_summer_white_top()

    await productsdetails.add_to_cart_click()

    await productsdetails.view_cart_click()

    product_elements = await viewcart.total_cart_boxes_all()
    product_count = len(product_elements)

    for i in range(product_count):
        product_name = await viewcart.get_product_price_element_by_index(i)
        assert "Men Tshirt" in product_name or "Summer White Top" in product_name
    print("registered user cart verification Successful")


    await loginhomepage.logout_button_click()

    await loginhome.menu_products_click()
    await products.click_brand_h3m()

    await brandproduct.click_brand_h3m_tshirt()

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
    print("non registered user cart verification Successful")