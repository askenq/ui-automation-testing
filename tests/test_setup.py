
import allure
from selenium.webdriver.support.ui import WebDriverWait


@allure.feature("Проверка окружения")
@allure.title("Главная страница сайта открывается")
def test_site_opens(driver):
    with allure.step("Открываем сайт"):
        driver.get("https://practice-automation.com/")

    with allure.step("Проверяем загрузку страницы"):
        WebDriverWait(driver, 15).until(
            lambda d: d.title.strip() != ""
        )

        assert driver.current_url.startswith(
            "https://practice-automation.com"
        )
        assert driver.title.strip() != ""
