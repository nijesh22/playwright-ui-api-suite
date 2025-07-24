import lorem
import pytest
import random
from flows.register_flow import register_new_user_flow
from utils.logger import Utils
from utils.test_data import generate_user_data

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_submit_product_review_valid_1(page,productsdetails,home,signup,createaccount,loginhome,products,brandproduct):
    user = generate_user_data()
    log = Utils.customlogger()

    await register_new_user_flow(page, home, signup, createaccount, user)

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
    log.info(" 'Thank You' message displayed successfully.")