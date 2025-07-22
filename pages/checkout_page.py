class CheckoutPage:
    def __init__(self, page):
        self.page = page

        self.delivery_address = page.locator("//ul[@id='address_delivery']")
        self.get_tshirt = page.locator("//a[normalize-space()='Men Tshirt']")
        self.total_amount = page.locator("tbody tr td:nth-child(4) p:nth-child(1)")
        self.place_order = page.locator("//a[normalize-space()='Place Order']")

    async def get_delivery_address(self):
        elements = self.delivery_address
        text = await elements.text_content()
        return text.strip()

    async def get_tshirt_text(self):
        elements = self.get_tshirt
        text = await elements.text_content()
        return text.strip()

    async def get_total_amount(self):
        elements = self.total_amount
        text = await elements.text_content()
        return text.strip()

    async def click_place_order(self):
        await self.place_order.click()





