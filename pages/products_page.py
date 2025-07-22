import time


class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.product_names = page.locator("//div[@class='productinfo text-center']//p")
        self.view_product = page.locator("//div[@class='choose']")
        self.products = page.locator("//div[@class='single-products']")
        self.products_search = page.locator("#search_product")
        self.products_search_button = page.locator("#submit_search")
        self.products_search_names_singles = page.locator("div[class='productinfo text-center'] p")
        self.category_men = page.locator("//a[normalize-space()='Men']")
        self.category_men_tshirt = page.locator("//a[normalize-space()='Tshirts']")
        self.brands_h3m = page.locator("//a[@href='/brand_products/H&M']")
        self.get_product_price = page.locator("//div[@class='productinfo text-center']//h2")
        self.get_product_img = page.locator("//div[@class='productinfo text-center']//img")

    async def get_product_images(self):
        count = await self.get_product_img.count()
        return [self.get_product_img.nth(i) for i in range(count)]


    async def get_product_price_element(self):
       return await self.get_product_price.all()

    async def get_product_price_element_by_index(self,index):
        elements = await self.get_product_price_element()
        text = await elements[index].text_content()
        return text

    async def get_product_element(self):
       return await self.product_names.all()

    async def get_product_element_by_index(self,index):
        elements = await self.get_product_element()
        text = await elements[index].text_content()
        return text

    async def get_product_element_singles(self):
       return await self.products_search_names_singles.all()

    async def get_product_element_by_index_search(self,index):
        elements1 = await self.get_product_element_singles()
        text1 = await elements1[index].text_content()
        return text1

    async def click_product_view(self):
       return await self.view_product.all()

    async def click_product_view_buttons_index(self,index):
        click_button = await self.click_product_view()
        await click_button[index].click()

    async def search_product(self,products_name_search):
        await self.products_search.fill(products_name_search)


    async def search_product_clear(self):
        await self.products_search.fill("")

    async def search_button_click(self):
        await self.products_search_button.click()

    async def products_all(self):
        return await self.products.all()

    async def search_product_name_get(self, product_name):
        await self.products_search.fill(product_name)
        filled_value = await self.products_search.input_value()
        return filled_value

    async def click_category_men(self):
        await self.category_men.click()

    async def click_category_men_tshirt(self):
        await self.category_men_tshirt.click()

    async def click_brand_h3m(self):
        await self.brands_h3m.click()





