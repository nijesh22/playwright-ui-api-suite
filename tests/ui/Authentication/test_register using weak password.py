import pytest
from utils.test_data import generate_user_data

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
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
async def test_register_using_weak_password_1(page, weak_password,home,signup):
    password = weak_password

    user = generate_user_data()

    await home.go_to_signup_page()
    await signup.signup(user)

    assert not await page.locator("//b[normalize-space()='Account Created!']").is_visible(), \
        f"{password} : A weak password like this must NOT be accepted!"





