
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ModalsPage:
    URL = "https://practice-automation.com/modals/"

    SIMPLE_MODAL_BUTTON = (By.ID, "simpleModal")
    FORM_MODAL_BUTTON = (By.ID, "formModal")
    ACTIVE_MODAL = (By.CSS_SELECTOR, ".pum-active")
    MODAL_CONTAINER = (By.CSS_SELECTOR, ".pum-active .pum-container")
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".pum-active .pum-close")

    NAME_INPUT = (By.ID, "g1051-name")
    EMAIL_INPUT = (By.ID, "g1051-email")
    MESSAGE_INPUT = (By.ID, "contact-form-comment-g1051-message")
    SUBMIT_BUTTON = (
        By.CSS_SELECTOR,
        ".pum-active button[type='submit']",
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(
            EC.visibility_of_element_located(self.SIMPLE_MODAL_BUTTON)
        )
        return self

    
    def open_simple_modal(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SIMPLE_MODAL_BUTTON)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.ACTIVE_MODAL)
        )


    def open_form_modal(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FORM_MODAL_BUTTON)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.MODAL_CONTAINER)
        )

    def is_modal_open(self):
        return any(
            element.is_displayed()
            for element in self.driver.find_elements(
                *self.ACTIVE_MODAL
            )
        )

    def close_modal(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CLOSE_BUTTON)
        ).click()

        self.wait.until(
            EC.invisibility_of_element_located(self.ACTIVE_MODAL)
        )

    def fill_form(self, name, email, message):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.MESSAGE_INPUT).send_keys(message)

    def submit_form(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()
