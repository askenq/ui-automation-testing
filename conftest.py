
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(3)

    yield browser

    # При ошибке теста прикладываем скриншот к Allure.
    if (
        getattr(request.node, "rep_call", None)
        and request.node.rep_call.failed
    ):
        try:
            screenshot = browser.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as error:
            print(f"Не удалось сохранить скриншот: {error}")

    browser.quit()
