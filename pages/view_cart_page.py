
class ViewCartPage:
    def __init__(self, page):
        self.page = page

        self.product_Tshirt = page.locator("//a[normalize-space()='Men Tshirt']")
        self.product_Tshirt_price = page.locator("//td[@class='cart_price']//p[contains(text(),'Rs. 400')]")
        self.cancel_cart_iteam = page.locator(".fa.fa-times")
        self.cart_is_empty_text = page.locator("//b[normalize-space()='Cart is empty!']")
        self.get_total_cart_titles = page.locator("//td[@class='cart_description']/h4")
        self.get_total_boxes = page.locator("//tbody/tr[starts-with(@id, 'product-')]")
        self.cart_quantity = page.locator("//button[@class='disabled']")
        self.proceed_to_checkout = page.locator("//a[normalize-space()='Proceed To Checkout']")
        self.register_or_login = page.locator("//u[normalize-space()='Register / Login']")

    async def register_or_login_click(self):
        await self.register_or_login.click()

    async def proceed_to_checkout_click(self):
        await self.proceed_to_checkout.click()

    async def get_cart_quantity(self):
        elements = self.cart_quantity
        text = await elements.text_content()
        return text

    async def get_product_tshirt(self):
        elements = self.product_Tshirt
        text = await elements.text_content()
        return text

    async def get_product_tshirt_price(self):
        elements = self.product_Tshirt_price
        text = await elements.text_content()
        return text

    async def click_cancel_cart_iteam(self):
        await self.cancel_cart_iteam.click()

    async def get_cart_is_empty_text(self):
        elements = self.cart_is_empty_text
        text = await elements.text_content()
        return text

    async def get_total_cart_titles_elements(self):
        return await self.get_total_cart_titles.all()

    async def get_product_price_element_by_index(self,index):
        elements = await self.get_total_cart_titles_elements()
        text = await elements[index].text_content()
        return text

    async def total_cart_boxes_all(self):
        return await self.get_total_boxes.all()



