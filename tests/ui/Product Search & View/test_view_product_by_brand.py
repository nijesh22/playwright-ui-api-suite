import pytest
from flows.brand_navigation_to_h3m_product_flow import go_to_brand_h3m_tshirt_and_assert_product

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_view_product_by_brand_1(page,loginhome,products,brandproduct):

    await loginhome.menu_products_click()

    await go_to_brand_h3m_tshirt_and_assert_product(page, products, brandproduct)
