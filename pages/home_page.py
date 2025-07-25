class HomePage:
    def __init__(self, page):
        self.page = page
        self.signup_login_button = page.locator("a[href='/login']")

    async def go_to_signup_page(self):
        await self.page.goto("https://automationexercise.com/" , wait_until="domcontentloaded", timeout=60000)
        await self.signup_login_button.click()
