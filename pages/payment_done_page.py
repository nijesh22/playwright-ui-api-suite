class PayementDonePage:
    def __init__(self, page):
        self.page = page

        self.order_placed_title = page.locator("h2[class='title text-center'] b")
        self.download_invoice = page.locator("//a[normalize-space()='Download Invoice']")

    async def get_order_placed_title(self):
        elements = self.order_placed_title
        text = await elements.text_content()
        return text

    async def click_download_invoice(self):
        await self.download_invoice.click()
