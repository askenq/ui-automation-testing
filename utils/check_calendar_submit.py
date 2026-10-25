
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


URL = "https://practice-automation.com/calendars/"
DATE_INPUT = (By.ID, "g1065-1-selectorenteradate")
SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        for value in ["2026-10-25", "", "not-a-date", "2026-02-30"]:
            print("\n" + "=" * 50)
            print("TEST VALUE:", repr(value))

            driver.get(URL)

            WebDriverWait(driver, 10).until(
                lambda d: d.find_element(*DATE_INPUT).is_displayed()
            )

            field = driver.find_element(*DATE_INPUT)
            field.clear()

            if value:
                field.send_keys(value)

            driver.find_element(*SUBMIT).click()

            WebDriverWait(driver, 10).until(
                lambda d: d.execute_script(
                    "return document.readyState"
                ) == "complete"
            )

            print("URL:", driver.current_url)
            print(
                "FIELD VALUE:",
                driver.find_element(*DATE_INPUT).get_attribute("value")
            )
            print(
                "BODY TEXT:",
                driver.find_element(By.TAG_NAME, "body").text[-1200:]
            )

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
