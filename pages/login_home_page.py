
class LoginHomePage:
    def __init__(self, page):
        self.page = page
        self.logout_button = page.locator("a[href='/logout']")
        self.delete_button = page.locator("a[href='/delete_account']")
        self.menu_products = page.locator("a[href='/products']")
        self.menu_carts = page.locator("//a[normalize-space()='Cart']")

    async def menu_cart_click(self):
        await self.menu_carts.click()

    async def logout_button_click(self):
        await self.logout_button.click()

    async def delete_button_click(self):
        await self.delete_button.click()

    async def menu_products_click(self):
        await self.page.goto("https://automationexercise.com/" , wait_until="domcontentloaded", timeout=60000)
        await self.menu_products.click()

