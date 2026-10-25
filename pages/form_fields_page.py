
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class FormFieldsPage:
    URL = "https://practice-automation.com/form-fields/"

    TOOLS_LABEL = (
        By.XPATH,
        "//*[normalize-space()='Automation tools']",
    )
    MESSAGE_FIELD = (
        By.CSS_SELECTOR,
        "textarea",
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(
            EC.visibility_of_element_located(self.TOOLS_LABEL)
        )
        return self

    def get_automation_tools(self):
        label = self.driver.find_element(*self.TOOLS_LABEL)

        # Находим элементы списка, относящиеся к Automation tools.
        container = label.find_element(
            By.XPATH,
            "./following-sibling::*[1]",
        )

        tools = container.find_elements(By.XPATH, ".//li")

        return [
            tool.text.strip()
            for tool in tools
            if tool.text.strip()
        ]

    def fill_message_with_tools(self):
        tools = self.get_automation_tools()

        if not tools:
            raise AssertionError(
                "Не удалось получить список Automation Tools"
            )

        message = ", ".join(tools)

        field = self.wait.until(
            EC.visibility_of_element_located(self.MESSAGE_FIELD)
        )
        field.clear()
        field.send_keys(message)

        return message
