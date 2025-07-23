class PayementPage:
    def __init__(self, page):
        self.page = page

        self.name_on_card = page.locator("//input[@name='name_on_card']")
        self.card_number = page.locator("input[name='card_number']")
        self.cvc = page.locator("input[placeholder='ex. 311']")
        self.Expiration = page.locator("input[placeholder='MM']")
        self.year = page.locator("input[placeholder='YYYY']")
        self.pay = page.locator("#submit")


    async def fill_name_on_card(self,name):
        await self.name_on_card.fill(name)

    async def fill_card_number(self,number):
        await self.card_number.fill(number)

    async def fill_cvc(self,cvc_data):
        await self.cvc.fill(cvc_data)

    async def fill_expiration(self,expiration_data):
        await self.Expiration.fill(expiration_data)

    async def year_fill(self,enter_year):
        await self.year.fill(enter_year)

    async def pay_and_order(self):
        await self.pay.click()

    async def fill_card_details(self, name, number, cvc, expiration_data, enter_year):
        await self.fill_name_on_card(name)
        await self.fill_card_number(number)
        await self.fill_cvc(cvc)
        await self.fill_expiration(expiration_data)
        await self.year_fill(enter_year)



