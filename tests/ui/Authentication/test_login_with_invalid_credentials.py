import pytest
from utils.assertions import assert_equal_validation_message

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_login_with_invalid_credentials_1(page,home,signup):

    validation_message = "Your email or password is incorrect!"

    await home.go_to_signup_page()
    await signup.login("invaliduser@test.com","invaliduser@8380")

    msg = await signup.login_page_validation_message()
    await assert_equal_validation_message(msg, validation_message)