import pytest
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.assertions import assert_verify_account_created
from utils.test_data import generate_user_data


@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_register_with_blank_fields_1(page):
    home = HomePage(page)
    signup = SignupPage(page)
    user = generate_user_data()

    await home.go_to_signup_page()
    await signup.signup(user)

    await assert_verify_account_created(page)
    print(f"Email: {user.email}")
    print(f"Password: {user.password}")



