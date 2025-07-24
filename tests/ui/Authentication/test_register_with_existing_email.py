import pytest

from utils.logger import Utils


@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_register_with_existing_email_1(page,home,signup):
    log = Utils.customlogger()

    await home.go_to_signup_page()
    await signup.signup_with_existing_email("TestUser","nijeshplaywright8493@test.com")

    msg = await signup.signup_page_validation_message()
    assert msg == "Email Address already exist!", f" Unexpected validation message: {msg}"
    log.info(" Validation message displayed correctly")


