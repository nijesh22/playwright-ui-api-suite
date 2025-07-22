
class BrandProductPage:
    def __init__(self, page):
        self.page = page

        self.brands_h3m_tshirt = page.locator("a[href='/product_details/2']")
        self.brands_summer_white_top = page.locator("a[href='/product_details/6']")

    async def click_brand_h3m_tshirt(self):
        await self.brands_h3m_tshirt.click()

    async def click_view_products_summer_white_top(self):
        await self.brands_summer_white_top.click()
