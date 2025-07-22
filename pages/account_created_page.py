
class CreateAccountPage:
    def __init__(self, page):
        self.page = page

        self.continue_button = page.locator("//a[normalize-space()='Continue']")

    async def continue_button_click(self):
        await self.continue_button.click()
