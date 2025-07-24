import pytest
from flows.register_flow import register_new_user_flow
from utils.assertions import assert_url
from utils.logger import Utils
from utils.test_data import generate_user_data

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_select_payment_method_1(page,payement,payementdone,viewcart,checkout,home,signup,createaccount,loginhome,productsdetails,brandproduct):
    user = generate_user_data()
    log = Utils.customlogger()

    await register_new_user_flow(page, home, signup, createaccount, user)

    await loginhome.menu_products_click()

    await productsdetails.add_to_cart_click()

    await page.go_back()

    await brandproduct.click_brand_h3m_tshirt()

    await productsdetails.add_to_cart_click()

    await productsdetails.view_cart_click()

    await viewcart.proceed_to_checkout_click()

    await checkout.click_place_order()

    await assert_url(page, "https://automationexercise.com/payment")

    await payement.fill_card_details("ram raj", "1234 1234 1234 1234", "123", "01", "2045")

    await payement.pay_and_order()

    payment_title = await payementdone.get_order_placed_title()

    assert payment_title == "Order Placed!" , "couldn't find the title"
    log.info("Successfully Verified Order Completion")
