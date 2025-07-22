import lorem
import pytest
import random
from pages.home_page import HomePage
from pages.signup_page import SignupPage

@pytest.mark.parametrize("page", ["chromium"], indirect=True)
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
async def test_register_using_weak_password_1(page, weak_password):
    home = HomePage(page)
    signup = SignupPage(page)

    name = "TestUser"
    email = f"nijeshplaywright{random.randint(1000,9999)}@test.com"
    password = weak_password
    first_name = f"nijesh{random.randint(100,999)}"
    last_name = f"playwright{random.randint(100,999)}"
    address = lorem.sentence()
    state= "ontario"
    city = "toronto"
    zipcode = "12345"
    mobile_no = "1234567890"

    await home.go_to_signup_page()
    await signup.signup(name,email,password,first_name,last_name,address,state,city,zipcode,mobile_no)

    assert not await page.locator("//b[normalize-space()='Account Created!']").is_visible(), \
        f"{password} : A weak password like this must NOT be accepted!"





