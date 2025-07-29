import pytest
from flows.register_flow import register_new_user_flow
from utils.test_data import generate_user_data

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_submit_product_review_empty_fields(page,productsdetails,brandproduct,products,home,loginhome,signup,createaccount,):
    user = generate_user_data()

    await register_new_user_flow(page, home, signup, createaccount, user)

    await loginhome.menu_products_click()
    await products.click_brand_h3m()

    await brandproduct.click_brand_h3m_tshirt()

    await productsdetails.review_name_fill("raju")
    await productsdetails.review_gmail_fill("")
    await productsdetails.review_box_fill("")

    await productsdetails.review_button_click()




