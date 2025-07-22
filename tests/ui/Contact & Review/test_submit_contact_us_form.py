import pytest
from pages.contact_us_page import ContactUsPage

@pytest.mark.parametrize("page", ["chromium"], indirect=True)
@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.asyncio
async def test_submit_contact_us_form_1(page):
    contactus = ContactUsPage(page)

    await contactus.go_to_contact_us_page()
    await contactus.fill_name("raju")
    await contactus.fill_email("raju@gmail.com")
    await contactus.fill_subject(" subject heading")
    await contactus.fill_message("hello how are you?")
    await contactus.upload_file_1("C:\\Users\\imnij\\Desktop\\uploadfile.txt")

    await contactus.click_submit_button()