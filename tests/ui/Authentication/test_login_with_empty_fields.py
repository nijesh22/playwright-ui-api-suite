import pytest
from utils.assertions import assert_required_field_blocked

@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_login_with_empty_fields_1(page,home,signup):
    await home.go_to_signup_page()

    blocked = await signup.login_is_required_field_blocking_submission()
    await assert_required_field_blocked(blocked)