import time

import allure
import pytest
from selenium.webdriver.common.by import By

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
@allure.title("На странице отображается описание обратного отсчёта")
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
@allure.title("Рекламное окно содержит ожидаемый текст")
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
@allure.title("Контейнер рекламы скрывается после закрытия")
def test_ad_container_is_hidden_after_close(ads):
    ads.wait_for_ad()
    ads.close_ad()

    containers = ads.driver.find_elements(*ads.ACTIVE_AD)

    assert all(
        not container.is_displayed()
        for container in containers
    )


@allure.feature("Ads")
@allure.title("Страница остаётся доступной после закрытия рекламы")
def test_page_remains_open_after_ad_close(ads):
    ads.wait_for_ad()
    ads.close_ad()

    assert "Ads" in ads.driver.title
    assert ads.driver.find_element(
        By.TAG_NAME, "body"
    ).is_displayed()


# Негативные тесты


@allure.feature("Ads")
@allure.title("В рекламном окне отсутствует посторонний текст")
def test_wrong_ad_text_is_not_displayed(ads):
    ad = ads.wait_for_ad()

    assert "This is not an advertisement." not in ad.text


@allure.feature("Ads")
@allure.title("Кнопка закрытия скрывается после закрытия рекламы")
def test_close_button_is_hidden_after_ad_close(ads):
    ads.wait_for_ad()
    ads.close_ad()

    buttons = ads.driver.find_elements(*ads.AD_CLOSE)

    assert not any(
        button.is_displayed()
        for button in buttons
    )


@allure.feature("Ads")
@allure.title("Закрытая реклама не появляется повторно")
def test_ad_does_not_reopen_after_close(ads):
    ads.wait_for_ad()
    ads.close_ad()

    # Проверяем, что в течение двух секунд реклама не появляется снова.
    time.sleep(2)

    assert not ads.is_ad_visible()