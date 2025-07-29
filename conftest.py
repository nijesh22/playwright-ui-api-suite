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



@pytest.fixture(scope="function", autouse=True)
async def trace_on_failure(page, request):
    # Start tracing
    await page.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    yield
    # Stop tracing only if test failed
    if request.node.rep_call.failed:
        await page.context.tracing.stop(path=f"{request.node.name}.zip")

# Hook to capture test result
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)



# conftest.py
import pytest
from playwright.async_api import async_playwright

# UI Fixture (provides a browser page)
@pytest.fixture
async def page(request):
    browser_name = getattr(request, 'param', 'chromium')  # defaults to chromium
    async with async_playwright() as p:
        browser = {
            "chromium": p.chromium,
            "firefox": p.firefox,
            "webkit": p.webkit
        }[browser_name]
        browser_instance = await browser.launch(headless=True, slow_mo=100)
        context = await browser_instance.new_context()
        page = await context.new_page()
        yield page
        await browser_instance.close()

# API Fixture (provides only request context)
@pytest.fixture
async def api_request():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        request_context = context.request
        yield request_context
        await browser.close()





