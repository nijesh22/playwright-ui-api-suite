class ProductsDetailsPage:
    def __init__(self, page):
        self.page = page
        self.product_details_page_title = page.locator("div[class='product-information'] h2")
        self.get_product_details_price = page.locator("div[class='product-information'] span span")
        self.review_name = page.locator("//input[@id='name']")
        self.review_email = page.locator("//input[@id='email']")
        self.review_box = page.locator("//textarea[@id='review']")
        self.review_button = page.locator("//button[@id='button-review']")
        self.review_thank_you_alert = page.locator("div[class='alert-success alert'] span")
        self.add_to_cart = page.locator("button[type='button']")
        self.view_cart = page.locator("//u[normalize-space()='View Cart']")

    async def get_product_details_element(self):
        elements = self.product_details_page_title
        text = await elements.text_content()
        return text

    async def get_product_details_price_element(self):
        elements = self.get_product_details_price
        text = await elements.text_content()
        return text

    async def review_name_fill(self,name):
        await self.review_name.fill(name)

    async def review_gmail_fill(self,gmail_address):
        await self.review_email.fill(gmail_address)

    async def review_box_fill(self,comment):
        await self.review_box.fill(comment)

    async def review_button_click(self):
        await self.review_button.click()

    async def get_thank_you_alert_text(self):
        elements = self.review_thank_you_alert
        text = await elements.text_content()
        return text

    async def add_to_cart_click(self):
        await self.add_to_cart.click()

    async def view_cart_click(self):
        await self.view_cart.click()