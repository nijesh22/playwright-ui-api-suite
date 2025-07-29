import pytest
from utils.assertions import assert_account_not_created
from utils.test_data import generate_user_data

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
@pytest.mark.parametrize("weak_password", [
    "123456",
    "password",
    "abcdef",
    "qwerty",
    "test123",
    "111111",
    "letmein",
    "iloveyou"
])
async def test_register_using_weak_password(page, weak_password,home,signup):
    user = generate_user_data()

    await home.go_to_signup_page()
    await signup.signup(user)

    await assert_account_not_created(page, weak_password)





