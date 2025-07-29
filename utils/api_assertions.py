import time

from utils.logger import Utils

log = Utils.customlogger()

async def assert_status_code(response, expected_code):
    assert response.status == expected_code, \
        f"Expected {expected_code}, got {response.status}"


async def assert_response_time_under(api_request, url = "https://fakestoreapi.com/products/1", max_seconds=2):
    start_time = time.perf_counter()
    response = await api_request.get(url)
    response_time = time.perf_counter() - start_time

    assert response_time < max_seconds, \
        f"⚠️ Response time too high: {response_time:.2f}s"

    print(f"✅ Response time OK: {response_time:.2f}s")
    return response

async def assert_status_code_and_response_time(response,api_request):
    await assert_status_code(response, 200)

    await assert_response_time_under(api_request, max_seconds=2)

