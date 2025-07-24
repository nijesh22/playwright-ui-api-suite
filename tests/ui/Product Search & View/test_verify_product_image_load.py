import pytest
from utils.assertions import assert_image_is_loaded

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_verify_product_image_load_1(page,loginhome,products):

    await loginhome.menu_products_click()

    images = await products.get_product_images()

    for img in images:
        await assert_image_is_loaded(img, label="Product image")

