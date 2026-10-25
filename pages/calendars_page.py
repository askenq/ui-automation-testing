
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalendarsPage:
    URL = "https://practice-automation.com/calendars/"

    DATE_INPUT = (By.ID, "g1065-1-selectorenteradate")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(
            EC.visibility_of_element_located(self.DATE_INPUT)
        )
        return self

    def enter_date(self, value):
        field = self.wait.until(
            EC.visibility_of_element_located(self.DATE_INPUT)
        )
        field.clear()
        field.send_keys(value)

    def submit(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()

    def get_date_value(self):
        return self.driver.find_element(
            *self.DATE_INPUT
        ).get_attribute("value")
