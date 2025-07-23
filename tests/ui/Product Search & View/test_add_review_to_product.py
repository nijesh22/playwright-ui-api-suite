import random
import lorem
import pytest
from pages.category_products_page import CategoryProductPage
from pages.login_home_page import LoginHomePage
from pages.product_details_page import ProductsDetailsPage
from pages.products_page import ProductsPage
from utils.assertions import assert_url

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_add_review_to_productz_1(page):

    loginhome = LoginHomePage(page)
    products = ProductsPage(page)
    categoryproduct = CategoryProductPage(page)
    productsdetails = ProductsDetailsPage(page)

    await loginhome.menu_products_click()
    await products.click_category_men()
    await products.click_category_men_tshirt()

    await assert_url(page, "https://automationexercise.com/category_products/3")

    await categoryproduct.mens_tshirt_click()

    await assert_url(page, "https://automationexercise.com/product_details/2")

    await productsdetails.review_name_fill( "raju")
    await productsdetails.review_gmail_fill(f"rajuplaywright{random.randint(1000,9999)}@test.com")
    await productsdetails.review_box_fill(lorem.sentence())

    await productsdetails.review_button_click()

    expected_validation = "Thank you for your review."
    actual_validation = await productsdetails.get_thank_you_alert_text()
    assert actual_validation == expected_validation, " 'Thank You' validation message is incorrect."
    print(" 'Thank You' message displayed successfully.")


