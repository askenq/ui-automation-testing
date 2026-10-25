import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.ads_page import AdsPage


@pytest.fixture
def ads(driver):
    return AdsPage(driver).open()


# Позитивные тесты


@allure.feature("Ads")
@allure.title("Страница рекламы открывается")
def test_ads_page_opens(ads):
    assert "Ads" in ads.driver.title


@allure.feature("Ads")
@allure.title("На странице есть описание обратного отсчёта")
def test_countdown_is_displayed(ads):
    body = ads.driver.find_element(By.TAG_NAME, "body").text
    assert "An ad will appear" in body


@allure.feature("Ads")
@allure.title("Рекламное окно появляется после ожидания")
def test_ad_appears(ads):
    ad = ads.wait_for_ad()
    assert ad.is_displayed()
    assert ad.text.strip() == "I am an ad."


@allure.feature("Ads")
@allure.title("Рекламное окно содержит текст")
def test_ad_has_expected_text(ads):
    ad = ads.wait_for_ad()
    assert "I am an ad." in ad.text


@allure.feature("Ads")
@allure.title("Кнопка закрытия рекламы отображается")
def test_ad_close_button_is_visible(ads):
    ads.wait_for_ad()
    button = ads.driver.find_element(*ads.AD_CLOSE)

    assert button.is_displayed()
    assert button.is_enabled()


@allure.feature("Ads")
@allure.title("Рекламное окно можно закрыть")
def test_ad_can_be_closed(ads):
    ads.wait_for_ad()
    ads.close_ad()

    assert not ads.is_ad_visible()


@allure.feature("Ads")
@allure.title("После закрытия рекламное окно скрыто")
def test_ad_container_is_hidden_after_close(ads):
    ads.wait_for_ad()
    ads.close_ad()

    containers = ads.driver.find_elements(*ads.ACTIVE_AD)
    assert all(not element.is_displayed() for element in containers)


@allure.feature("Ads")
@allure.title("Страница остаётся доступной после закрытия рекламы")
def test_page_remains_open_after_ad_close(ads):
    ads.wait_for_ad()
    ads.close_ad()

    assert "Ads" in ads.driver.title
    assert ads.driver.find_element(By.TAG_NAME, "body").is_displayed()


# Негативные тесты


@allure.feature("Ads")
@allure.title("Несуществующий рекламный текст не находится")
def test_nonexistent_ad_text_is_not_found(ads):
    ads.wait_for_ad()

    elements = ads.driver.find_elements(
        By.XPATH,
        "//*[normalize-space(.)='This advertisement does not exist']",
    )

    assert not any(element.is_displayed() for element in elements)


@allure.feature("Ads")
@allure.title("Несуществующая кнопка закрытия не находится")
def test_nonexistent_close_button_is_not_found(ads):
    ads.wait_for_ad()

    elements = ads.driver.find_elements(
        By.ID,
        "nonexistent-ad-close-button",
    )

    assert len(elements) == 0


@allure.feature("Ads")
@allure.title("Рекламное окно не остаётся открытым после закрытия")
def test_ad_is_not_visible_after_close(ads):
    ads.wait_for_ad()
    ads.close_ad()

    WebDriverWait(ads.driver, 5).until(
        lambda driver: not ads.is_ad_visible()
    )

    assert not ads.is_ad_visible()
