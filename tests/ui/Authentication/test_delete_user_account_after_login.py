import pytest
from pages.account_created_page import CreateAccountPage
from pages.delete_account_page import DeleteAccountPage
from pages.home_page import HomePage
from pages.login_home_page import LoginHomePage
from pages.signup_page import SignupPage
from utils.assertions import assert_equal_validation_message, assert_url
from utils.test_data import generate_user_data


@pytest.mark.parametrize("page", ["chromium"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_delete_user_account_after_login_1(page):
    home = HomePage(page)
    signup = SignupPage(page)
    loginhome = LoginHomePage(page)
    deleteaccount = DeleteAccountPage(page)
    createaccount = CreateAccountPage(page)

    user = generate_user_data()

    expected_url = "https://automationexercise.com/"

    await home.go_to_signup_page()
    await signup.signup(user)

    assert await page.locator("//b[normalize-space()='Account Created!']").is_visible()
    print("Account successfully created")

    await createaccount.continue_button_click()

    await loginhome.delete_button_click()

    msg = await deleteaccount.delete_confirmation_text()
    validation_message = "Account Deleted!"

    await assert_equal_validation_message(msg, validation_message)

    await deleteaccount.continue_button_click()

    actual_url = page.url
    await assert_url(actual_url, expected_url)
