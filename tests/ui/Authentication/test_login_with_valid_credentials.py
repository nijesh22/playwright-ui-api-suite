import pytest
from utils.assertions import assert_url

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_login_with_valid_credentials(page,home,signup):
    await home.go_to_signup_page()
    await signup.login("nijeshplaywright8163@test.com","qwerty@8380")

    await assert_url(page,"https://automationexercise.com/")
