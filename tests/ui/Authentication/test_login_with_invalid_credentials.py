import pytest
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.assertions import assert_equal_validation_message

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_login_with_invalid_credentials_1(page):
    home = HomePage(page)
    signup = SignupPage(page)

    validation_message = "Your email or password is incorrect!"

    await home.go_to_signup_page()
    await signup.login("invaliduser@test.com","invaliduser@8380")

    msg = await signup.login_page_validation_message()
    await assert_equal_validation_message(msg, validation_message)