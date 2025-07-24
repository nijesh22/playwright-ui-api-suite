import pytest
import allure
import asyncio
from playwright.async_api import async_playwright
from pages.account_created_page import CreateAccountPage
from pages.brand_products_page import BrandProductPage
from pages.category_products_page import CategoryProductPage
from pages.checkout_page import CheckoutPage
from pages.contact_us_page import ContactUsPage
from pages.delete_account_page import DeleteAccountPage
from pages.home_page import HomePage
from pages.login_home_page import LoginHomePage
from pages.payement_page import PayementPage
from pages.payment_done_page import PayementDonePage
from pages.product_details_page import ProductsDetailsPage
from pages.products_page import ProductsPage
from pages.signup_page import SignupPage
from pages.view_cart_page import ViewCartPage


@pytest.fixture
async def page(request):
    browser_name = request.param  # passed via @pytest.mark.parametrize
    async with async_playwright() as p:
        browser = {
            "chromium": p.chromium,
            "firefox": p.firefox,
            "webkit": p.webkit  # WebKit covers Safari/Edge scenarios
        }[browser_name]

        browser_instance = await browser.launch(headless=False, slow_mo=500)
        page = await browser_instance.new_page()
        yield page
        await browser_instance.close()

@pytest.fixture
def home(page):
    return HomePage(page)

@pytest.fixture
def signup(page):
    return SignupPage(page)

@pytest.fixture
def loginhome(page):
    return LoginHomePage(page)

@pytest.fixture
def deleteaccount(page):
    return DeleteAccountPage(page)

@pytest.fixture
def createaccount(page):
    return CreateAccountPage(page)

@pytest.fixture
def products(page):
    return ProductsPage(page)

@pytest.fixture
def brandproduct(page):
    return BrandProductPage(page)

@pytest.fixture
def productsdetails(page):
    return ProductsDetailsPage(page)

@pytest.fixture
def viewcart(page):
    return ViewCartPage(page)

@pytest.fixture
def checkout(page):
    return CheckoutPage(page)

@pytest.fixture
def payement(page):
    return PayementPage(page)

@pytest.fixture
def payementdone(page):
    return PayementDonePage(page)

@pytest.fixture
def contactus(page):
    return ContactUsPage(page)

@pytest.fixture
def categoryproduct(page):
    return CategoryProductPage(page)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")
        if page:

            loop = asyncio.get_event_loop()
            screenshot = loop.run_until_complete(page.screenshot())
            allure.attach(screenshot, name="screenshot_on_failure", attachment_type=allure.attachment_type.PNG)



