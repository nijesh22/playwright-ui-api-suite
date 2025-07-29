from utils.logger import Utils

log = Utils.customlogger()

async def assert_url(page,expected_url):
    actual_url = page.url
    assert actual_url == expected_url, f"Expected url '{expected_url}', but got '{actual_url}'"
    log.info(f" Navigated to correct URL {expected_url} item(s).")

async def assert_equal_validation_message(actual, expected, message=""):
    assert actual == expected, f"❌ {message or 'Unexpected validation message'}\nExpected: '{expected}'\nGot: '{actual}'"
    log.info(f" {message or 'Validation message displayed correctly'}")

async def assert_required_field_blocked(blocked):
    assert blocked, " Browser allowed submission with empty required fields"
    log.info(f"Native validation blocked empty submission!")

async def assert_equal_titles(actual, expected, message=""):
    assert actual == expected, f"❌ {message or 'Title Mismatch '}\nExpected: '{expected}'\nGot: '{actual}'"
    log.info(f"{expected} :Title displayed correctly")

async def assert_equal_prices(product_price, product_details_price):
    assert product_price == product_details_price,f"price Mismatch \n Expected: '{product_details_price}"
    log.info(f"{product_details_price} :price displayed correctly")

async def assert_image_is_loaded(image_element, label="Product image"):
    await image_element.scroll_into_view_if_needed()

    await image_element.page.wait_for_timeout(500)
    is_visible = await image_element.is_visible()
    assert is_visible, f"❌ {label} is not visible on the page."
    log.info(f" {label} is visible.")

async def assert_verify_account_created(page):
    locator = page.locator("//b[normalize-space()='Account Created!']")
    assert await locator.is_visible(), "Account creation confirmation not visible."
    log.info(" Account successfully created")

async def assert_text_match(actual, expected, label: str):
    assert actual == expected, f"{label} does not match expected value."
    log.info(f" {label} verified.")

async def assert_account_not_created(page, password: str):

    is_visible = await page.locator("text=Account Created!").is_visible()
    assert not is_visible, f"{password} : A weak password like this must NOT be accepted!"



