import json

import pytest

from utils.api_assertions import assert_status_code, assert_response_time_under, assert_status_code_and_response_time
from utils.api_helper import get_json_and_print
from utils.config import BASE_URL
from utils.payloads import create_put_payload


@pytest.mark.asyncio
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
async def test_post_products(api_request):

    payload = create_put_payload()
    url = f"{BASE_URL}/products/1"
    response = await api_request.put(url,data=json.dumps(payload),headers={"Content-Type": "application/json"})

    await assert_status_code_and_response_time(response, api_request)
    await get_json_and_print(response)