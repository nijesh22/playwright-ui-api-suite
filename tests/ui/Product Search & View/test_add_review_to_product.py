import random
import lorem
import pytest
from utils.assertions import assert_url
from utils.logger import Utils

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_add_review_to_productz(page,loginhome,products,productsdetails,categoryproduct):
    log = Utils.customlogger()

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
    log.info(" 'Thank You' message displayed successfully.")


