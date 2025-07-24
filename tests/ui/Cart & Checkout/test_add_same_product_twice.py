import pytest
from flows.brand_navigation_to_h3m_product_flow import go_to_brand_h3m_tshirt_and_assert_product
from flows.register_flow import register_new_user_flow
from utils.logger import Utils
from utils.test_data import generate_user_data

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_add_same_product_twice_1(page,home,signup,createaccount,loginhome,productsdetails,brandproduct,viewcart,products):
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

    quantity = await viewcart.get_cart_quantity()
    assert quantity.strip() == "2"
    log.info(f"{quantity} : Quantity successfully verified! ")


