import pytest
from utils.assertions import assert_image_is_loaded

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_verify_product_image_load(page,loginhome,products):

    await loginhome.menu_products_click()

    images = await products.get_product_images()

    for img in images:
        await assert_image_is_loaded(img, label="Product image")

