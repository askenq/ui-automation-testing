
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://practice-automation.com/ads/")

        WebDriverWait(driver, 15).until(
            lambda d: any(
                e.is_displayed()
                for e in d.find_elements(
                    By.XPATH,
                    "//*[normalize-space(text())='I am an ad.']"
                )
            )
        )

        print("AD ELEMENTS:")
        elements = driver.find_elements(
            By.XPATH,
            "//*[normalize-space(text())='I am an ad.']"
        )

        for element in elements:
            print(
                "TAG:", element.tag_name,
                "| ID:", element.get_attribute("id"),
                "| CLASS:", element.get_attribute("class"),
            )
            print(
                "PARENT:",
                element.find_element(By.XPATH, "..").get_attribute("outerHTML")[:1500]
            )

        print("\nVISIBLE CLOSE BUTTONS:")
        for element in driver.find_elements(
            By.CSS_SELECTOR,
            "button, a, [role='button']"
        ):
            if element.is_displayed():
                text = element.text.strip()
                aria = element.get_attribute("aria-label")
                title = element.get_attribute("title")

                if text in ("×", "X", "✕") or aria or title:
                    print(
                        "TAG:", element.tag_name,
                        "| TEXT:", repr(text),
                        "| ARIA:", aria,
                        "| TITLE:", title,
                        "| CLASS:", element.get_attribute("class"),
                    )

        input("\nНажми Enter для закрытия браузера...")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
