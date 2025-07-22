import pytest
from pages.home_page import HomePage
from pages.login_home_page import LoginHomePage
from pages.signup_page import SignupPage
from utils.assertions import assert_url

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_logout_from_the_system_1(page):
    home = HomePage(page)
    signup = SignupPage(page)
    loginhomepage = LoginHomePage(page)

    id = "nijeshplaywright8163@test.com"
    name = "qwerty@8380"
    expected_url = "https://automationexercise.com/"
    expected_url_final = "https://automationexercise.com/login"

    await home.go_to_signup_page()
    await signup.login(id,name)
    actual_url = page.url
    await assert_url(actual_url,expected_url)

    await loginhomepage.logout_button_click()
    actual_url = page.url
    await assert_url(actual_url, expected_url_final)