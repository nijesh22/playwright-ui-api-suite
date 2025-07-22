class ContactUsPage:
    def __init__(self, page):
        self.page = page
        self.menu_contact_us = page.locator("//a[normalize-space()='Contact us']")
        self.name = page.locator("input[placeholder='Name']")
        self.Email = page.locator("input[placeholder='Email']")
        self.subject = page.locator("input[placeholder='Subject']")
        self.message = page.locator("#message")
        self.choose_file = page.locator("input[name='upload_file']")
        self.submit = page.locator("input[data-qa='submit-button']")

    async def go_to_contact_us_page(self):
        await self.page.goto("https://automationexercise.com/")
        await self.menu_contact_us.click()

    async def fill_name(self,name):
       await self.name.fill(name)

    async def fill_email(self,email):
       await self.Email.fill(email)

    async def fill_subject(self,subject):
       await self.subject.fill(subject)

    async def fill_message(self, message):
        await self.message.fill(message)

    async def upload_file_1(self,input_file):
        await self.choose_file.set_input_files(input_file)

    async def click_submit_button(self):
        await self.submit.evaluate("window.scrollBy(0, 1000)")
        await self.submit.click()









