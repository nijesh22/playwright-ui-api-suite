import pytest
from pages.home_page import HomePage
from pages.signup_page import SignupPage

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_register_with_blank_fields(page):
    home = HomePage(page)
    signup = SignupPage(page)

    await home.go_to_signup_page()
    blocked = await signup.is_required_field_blocking_submission()
    assert blocked, " Browser allowed submission with empty required fields"
    print(" Native validation blocked empty form submission")

