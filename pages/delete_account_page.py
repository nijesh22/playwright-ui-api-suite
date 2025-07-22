
class DeleteAccountPage:
    def __init__(self, page):
        self.page = page
        self.delete_confirmation_message = page.locator("//b[normalize-space()='Account Deleted!']")
        self.continue_button = page.locator("//a[normalize-space()='Continue']")

    async def delete_confirmation_text(self):
        text = await self.delete_confirmation_message.text_content()
        return text.strip() if text else ""

    async def continue_button_click(self):
        await self.continue_button.click()


