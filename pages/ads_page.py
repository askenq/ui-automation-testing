
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AdsPage:
    URL = "https://practice-automation.com/ads/"

    AD_TEXT = (
        By.XPATH,
        "//p[normalize-space(.)='I am an ad.']",
    )
    AD_CLOSE = (
        By.CSS_SELECTOR,
        ".pum-active .pum-close[aria-label='Close']",
    )
    ACTIVE_AD = (
        By.CSS_SELECTOR,
        ".pum-active .pum-container",
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "body"))
        )
        return self

    def wait_for_ad(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.AD_TEXT)
        )

    def is_ad_visible(self):
        return any(
            element.is_displayed()
            for element in self.driver.find_elements(*self.AD_TEXT)
        )

    def close_ad(self):
        self.wait.until(
            EC.element_to_be_clickable(self.AD_CLOSE)
        ).click()

        self.wait.until(
            EC.invisibility_of_element_located(self.ACTIVE_AD)
        )
