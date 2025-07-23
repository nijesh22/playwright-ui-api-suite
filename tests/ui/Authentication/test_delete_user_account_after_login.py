import pytest
from pages.account_created_page import CreateAccountPage
from pages.delete_account_page import DeleteAccountPage
from pages.home_page import HomePage
from pages.login_home_page import LoginHomePage
from pages.signup_page import SignupPage
from utils.assertions import assert_equal_validation_message, assert_url
from utils.test_data import generate_user_data
from utils.assertions import assert_verify_account_created

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_delete_user_account_after_login_1(page):
    home = HomePage(page)
    signup = SignupPage(page)
    loginhome = LoginHomePage(page)
    deleteaccount = DeleteAccountPage(page)
    createaccount = CreateAccountPage(page)

    user = generate_user_data()

    await home.go_to_signup_page()
    await signup.signup(user)

    await assert_verify_account_created(page)

    await createaccount.continue_button_click()

    await loginhome.delete_button_click()

    msg = await deleteaccount.delete_confirmation_text()

    await assert_equal_validation_message(msg, "Account Deleted!")

    await deleteaccount.continue_button_click()

    await assert_url(page,"https://automationexercise.com/")