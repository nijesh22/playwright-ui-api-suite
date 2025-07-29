import pytest
from utils.api_assertions import assert_status_code_and_response_time
from utils.api_helper import get_json_and_print
from utils.config import BASE_URL

@pytest.mark.asyncio
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
async def test_get_product_category_jewelery(api_request):
    url = f"{BASE_URL}/products/category/jewelery"
    response = await api_request.get(url)

    await assert_status_code_and_response_time(response, api_request)
    await get_json_and_print(response)
