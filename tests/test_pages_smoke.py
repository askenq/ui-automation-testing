
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


PAGES = [
    (
        "Calendars",
        "https://practice-automation.com/calendars/",
        "Calendars",
    ),
    (
        "Modals",
        "https://practice-automation.com/modals/",
        "Modals",
    ),
    (
        "Ads",
        "https://practice-automation.com/ads/",
        "Ads",
    ),
]


@pytest.mark.parametrize(
    "page_name,url,expected_title",
    PAGES,
    ids=["Calendars", "Modals", "Ads"],
)
@allure.feature("Проверка страниц")
@allure.title("Страница {page_name} открывается")
def test_page_opens(driver, page_name, url, expected_title):
    with allure.step(f"Открываем страницу {page_name}"):
        driver.get(url)

    with allure.step("Ожидаем загрузки страницы"):
        WebDriverWait(driver, 15).until(
            lambda browser: browser.find_element(
                By.TAG_NAME, "body"
            ).text.strip() != ""
        )

    with allure.step("Проверяем заголовок страницы"):
        assert expected_title.lower() in driver.title.lower(), (
            f"Ожидался заголовок с текстом "
            f"'{expected_title}', получен: '{driver.title}'"
        )
