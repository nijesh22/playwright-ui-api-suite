import lorem
import pytest
import random
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.test_data import generate_user_data


@pytest.mark.parametrize("page", ["chromium"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_register_with_blank_fields_1(page):
    home = HomePage(page)
    signup = SignupPage(page)
    user = generate_user_data()


    await home.go_to_signup_page()
    await signup.signup(user)

    assert await page.locator("//b[normalize-space()='Account Created!']").is_visible()
    print("Account successfully created")

    print(f"Email: {user.email}")
    print(f"Password: {user.password}")



