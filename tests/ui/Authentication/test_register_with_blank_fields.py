import pytest
from utils.logger import Utils

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_register_with_blank_fields(page,home,signup):
    log = Utils.customlogger()

    await home.go_to_signup_page()
    blocked = await signup.is_required_field_blocking_submission()
    assert blocked, " Browser allowed submission with empty required fields"
    log.info(" Native validation blocked empty form submission")

