import os
import pytest

@pytest.mark.flaky(reruns=2, reruns_delay=1)
@pytest.mark.parametrize("page", ["chromium", "firefox", "webkit"], indirect=True)
#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_submit_contact_us_form_1(page,contactus):

    await contactus.go_to_contact_us_page()
    await contactus.fill_name("raju")
    await contactus.fill_email("raju@gmail.com")
    await contactus.fill_subject(" subject heading")
    await contactus.fill_message("hello how are you?")
    filepath = os.path.join(os.getcwd(), "test_data", "uploadfile.txt")
    await contactus.upload_file_1(filepath)

    await contactus.click_submit_button()