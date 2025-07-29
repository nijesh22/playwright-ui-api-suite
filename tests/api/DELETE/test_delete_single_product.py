import pytest
from utils.config import BASE_URL

#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_delete_single_product(api_request):
    url = f"{BASE_URL}/products/1"
    response = await api_request.delete(url)

    assert response.status == 204, f"Unexpected status: {response.status}"


