import pytest
from pages.home_page import HomePage
from pages.signup_page import SignupPage

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_register_with_existing_email_1(page):
    home = HomePage(page)
    signup = SignupPage(page)

    name = "TestUser"
    email = "nijeshplaywright8493@test.com"

    await home.go_to_signup_page()
    await signup.signup_with_existing_email(name,email)

    msg = await signup.signup_page_validation_message()
    assert msg == "Email Address already exist!", f" Unexpected validation message: {msg}"
    print(" Validation message displayed correctly")


