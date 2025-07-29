import pytest
from flows.delete_account_flow import delete_account_and_verify
from utils.test_data import generate_user_data
from utils.assertions import assert_verify_account_created

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_delete_user_account_after_login(page,home,signup,createaccount,loginhome,deleteaccount):
    user = generate_user_data()

    await home.go_to_signup_page()
    await signup.signup(user)

    await assert_verify_account_created(page)

    await createaccount.continue_button_click()

    await delete_account_and_verify(page, loginhome, deleteaccount)