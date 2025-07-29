import pytest
from utils.assertions import assert_url

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_logout_from_the_system(page,home,signup,loginhome):

    await home.go_to_signup_page()
    await signup.login("nijeshplaywright8163@test.com","qwerty@8380")

    await assert_url(page,"https://automationexercise.com/")

    await loginhome.logout_button_click()

    await assert_url(page, "https://automationexercise.com/login")