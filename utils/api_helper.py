async def get_json_and_print(response):
    json_data = await response.json()
    print(json_data)
    return json_data