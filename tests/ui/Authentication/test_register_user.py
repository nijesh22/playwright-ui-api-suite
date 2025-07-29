import pytest
from utils.assertions import assert_verify_account_created
from utils.logger import Utils
from utils.test_data import generate_user_data

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_register_with_blank_fields(page,home,signup):
    log = Utils.customlogger()
    user = generate_user_data()

    await home.go_to_signup_page()
    await signup.signup(user)

    await assert_verify_account_created(page)
    log.info(f"Email: {user.email}")
    log.info(f"Password: {user.password}")



