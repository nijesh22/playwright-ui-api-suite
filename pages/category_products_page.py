
class CategoryProductPage:
    def __init__(self, page):
        self.page = page

        self.mens_tshirt = page.locator("a[href='/product_details/2']")

    async def mens_tshirt_click(self):
        await self.mens_tshirt.click()
