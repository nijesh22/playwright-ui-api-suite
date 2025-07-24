import pytest
from flows.brand_navigation_to_h3m_product_flow import go_to_brand_h3m_tshirt_and_assert_product
from flows.register_flow import register_new_user_flow
from utils.assertions import assert_url
from utils.logger import Utils
from utils.test_data import generate_user_data

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_verify_order_summary_1(page,home,checkout,viewcart,productsdetails,signup,createaccount,loginhome,products,brandproduct):
    log = Utils.customlogger()
    user = generate_user_data()

    await register_new_user_flow(page, home, signup, createaccount, user)

    await loginhome.menu_products_click()

    await go_to_brand_h3m_tshirt_and_assert_product(page, products, brandproduct)

    await productsdetails.add_to_cart_click()

    await page.go_back()

    await brandproduct.click_brand_h3m_tshirt()

    await productsdetails.add_to_cart_click()

    await productsdetails.view_cart_click()

    await viewcart.proceed_to_checkout_click()

    await assert_url(page, "https://automationexercise.com/checkout")

    product_name = await checkout.get_tshirt_text()

    assert "Men Tshirt" in product_name , "Couldn't find Tshirt in Checkout"
    log.info("Mens Tshirt found!")

    total_amount = await checkout.get_total_amount()

    assert "Rs. 800" in total_amount, "found incorrect amount!"
    log.info("verified the Total amount correctly!")