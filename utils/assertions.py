

async def assert_url(actual_url, expected_url):
    assert actual_url == expected_url, f"Expected url '{expected_url}', but got '{actual_url}'"
    print(f"✅ Navigated to correct URL {expected_url} item(s).")

async def assert_equal_validation_message(actual, expected, message=""):
    assert actual == expected, f"❌ {message or 'Unexpected validation message'}\nExpected: '{expected}'\nGot: '{actual}'"
    print(f"✅ {message or 'Validation message displayed correctly'}")

async def assert_required_field_blocked(blocked):
    assert blocked, " Browser allowed submission with empty required fields"
    print(f"Native validation blocked empty submission!")

async def assert_equal_titles(actual, expected, message=""):
    assert actual == expected, f"❌ {message or 'Title Mismatch '}\nExpected: '{expected}'\nGot: '{actual}'"
    print(f"{expected} :Title displayed correctly")

async def assert_equal_prices(product_price, product_details_price):
    assert product_price == product_details_price,f"price Mismatch \n Expected: '{product_details_price}"
    print(f"{product_details_price} :price displayed correctly")

async def assert_image_is_loaded(image_element, label="Product image"):
    await image_element.scroll_into_view_if_needed()

    await image_element.page.wait_for_timeout(500)
    is_visible = await image_element.is_visible()
    assert is_visible, f"❌ {label} is not visible on the page."
    print(f"✅ {label} is visible.")
