import random

import lorem

from utils.test_data import UserData


class SignupPage:
    def __init__(self, page):
        self.page = page
        self.name_input = page.locator("input[placeholder='Name']")
        self.email_input = page.locator("input[data-qa='signup-email']")
        self.signup_button = page.locator("button[data-qa='signup-button']")
        self.title_mr = page.locator("#id_gender1")
        self.password_input = page.locator("#password")
        self.day = page.locator("#days")
        self.month = page.locator("#months")
        self.year = page.locator("#years")
        self.first_name = page.locator("#first_name")
        self.last_name = page.locator("#last_name")
        self.address = page.locator("#address1")
        self.country = page.locator("#country")
        self.state = page.locator("#state")
        self.city = page.locator("#city")
        self.zipcode = page.locator("#zipcode")
        self.mobile_no = page.locator("#mobile_number")
        self.create_account_button = page.locator("button[data-qa='create-account']")
        self.signup_validation_message = page.locator("//p[normalize-space()='Email Address already exist!']")
        self.login_id = page.locator("input[data-qa='login-email']")
        self.login_password = page.locator("input[placeholder='Password']")
        self.login_button = page.locator("button[data-qa='login-button']")
        self.login_validation_message = page.locator("//p[normalize-space()='Your email or password is incorrect!']")


    async def signup(self, user: UserData):
        await self.name_input.fill(user.name)
        await self.email_input.fill(user.email)
        await self.signup_button.click()
        await self.title_mr.click()
        await self.password_input.fill(user.password)
        await self.day.select_option('1')
        await self.month.select_option('January')
        await self.year.select_option('2000')
        await self.first_name.fill(user.first_name)
        await self.last_name.fill(user.last_name)
        await self.address.fill(user.address)
        await self.country.select_option('Canada')
        await self.state.fill(user.state)
        await self.city.fill(user.city)
        await self.zipcode.fill(user.zipcode)
        await self.mobile_no.fill(user.mobile_no)
        await self.create_account_button.click()


    async def signup_with_existing_email(self, name,email):
        await self.name_input.fill(name)
        await self.email_input.fill(email)
        await self.signup_button.click()

    async def signup_page_validation_message(self):
       text = await self.signup_validation_message.text_content()
       return text.strip() if text else ""

    async def is_required_field_blocking_submission(self):
        current_url = self.page.url
        await self.signup_button.click()
        return self.page.url == current_url

    async def login(self,id,password):
        await self.login_id.fill(id)
        await self.login_password.fill(password)
        await self.login_button.click()

    async def login_page_validation_message(self):
       text = await self.login_validation_message.text_content()
       return text.strip() if text else ""


    async def login_is_required_field_blocking_submission(self):
        current_url = self.page.url
        await self.login_button.click()
        return self.page.url == current_url




