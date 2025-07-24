from utils.assertions import assert_url

async def go_to_brand_h3m_tshirt_and_assert_product(page, products, brandproduct):
    await products.click_brand_h3m()
    await assert_url(page, "https://automationexercise.com/brand_products/H&M")
    await brandproduct.click_brand_h3m_tshirt()
    await assert_url(page, "https://automationexercise.com/product_details/2")
