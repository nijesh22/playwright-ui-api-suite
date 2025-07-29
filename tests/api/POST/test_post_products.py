import json
import pytest
from utils.api_helper import get_json_and_print
from utils.config import BASE_URL
from utils.payloads import create_post_payload

@pytest.mark.asyncio
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
async def test_post_products(api_request):

    payload = create_post_payload()
    url = f"{BASE_URL}/products"
    response = await api_request.post(url,data=json.dumps(payload),headers={"Content-Type": "application/json"})

    assert response.status in [200, 201], f"Unexpected status: {response.status}"
    await get_json_and_print(response)