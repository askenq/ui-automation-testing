
import allure

from pages.form_fields_page import FormFieldsPage


EXPECTED_TOOLS = [
    "Selenium",
    "Playwright",
    "Cypress",
    "Appium",
    "Katalon Studio",
]


@allure.feature("Form Fields")
@allure.title(
    "Поле Message заполняется списком Automation Tools"
)
def test_message_filled_with_automation_tools(driver):
    page = FormFieldsPage(driver).open()

    with allure.step("Получаем список Automation Tools через Selenium"):
        tools = page.get_automation_tools()
        assert tools == EXPECTED_TOOLS

    with allure.step("Заполняем поле Message списком через запятую"):
        message = page.fill_message_with_tools()

    with allure.step("Проверяем содержимое поля Message"):
        expected_message = ", ".join(EXPECTED_TOOLS)
        assert message == expected_message

        field = driver.find_element(*page.MESSAGE_FIELD)
        assert field.get_attribute("value") == expected_message
