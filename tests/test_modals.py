
import allure
import pytest
from selenium.webdriver.common.by import By

from pages.modals_page import ModalsPage


@pytest.fixture
def modals(driver):
    return ModalsPage(driver).open()


# Позитивные тесты


@allure.feature("Modals")
@allure.title("Страница модальных окон открывается")
def test_modals_page_opens(modals):
    assert "Modals" in modals.driver.title


@allure.feature("Modals")
@allure.title("Кнопка простого модального окна отображается")
def test_simple_modal_button_visible(modals):
    button = modals.driver.find_element(
        *modals.SIMPLE_MODAL_BUTTON
    )

    assert button.is_displayed()
    assert button.is_enabled()


@allure.feature("Modals")
@allure.title("Простое модальное окно открывается")
def test_simple_modal_opens(modals):
    modals.open_simple_modal()

    assert modals.is_modal_open()


@allure.feature("Modals")
@allure.title("Кнопка формы отображается")
def test_form_modal_button_visible(modals):
    button = modals.driver.find_element(
        *modals.FORM_MODAL_BUTTON
    )

    assert button.is_displayed()
    assert button.is_enabled()


@allure.feature("Modals")
@allure.title("Модальное окно с формой открывается")
def test_form_modal_opens(modals):
    modals.open_form_modal()

    assert modals.is_modal_open()
    assert modals.driver.find_element(
        *modals.NAME_INPUT
    ).is_displayed()
    assert modals.driver.find_element(
        *modals.EMAIL_INPUT
    ).is_displayed()
    assert modals.driver.find_element(
        *modals.MESSAGE_INPUT
    ).is_displayed()


@allure.feature("Modals")
@allure.title("Форма принимает текстовые данные")
def test_form_accepts_input(modals):
    modals.open_form_modal()

    modals.fill_form(
        "Alex",
        "alex@example.com",
        "Testing modal form",
    )

    assert modals.driver.find_element(
        *modals.NAME_INPUT
    ).get_attribute("value") == "Alex"

    assert modals.driver.find_element(
        *modals.EMAIL_INPUT
    ).get_attribute("value") == "alex@example.com"

    assert modals.driver.find_element(
        *modals.MESSAGE_INPUT
    ).get_attribute("value") == "Testing modal form"


@allure.feature("Modals")
@allure.title("Форму можно закрыть крестиком")
def test_form_modal_closes(modals):
    modals.open_form_modal()
    modals.close_modal()

    assert not modals.is_modal_open()


@allure.feature("Modals")
@allure.title("Форма содержит кнопку отправки")
def test_form_submit_button_visible(modals):
    modals.open_form_modal()

    button = modals.driver.find_element(
        *modals.SUBMIT_BUTTON
    )

    assert button.is_displayed()
    assert button.is_enabled()


# Негативные тесты


@allure.feature("Modals")
@allure.title("Пустое обязательное поле имени не проходит валидацию")
def test_empty_name_fails_validation(modals):
    modals.open_form_modal()
    modals.fill_form(
        "",
        "alex@example.com",
        "Test message",
    )

    name = modals.driver.find_element(
        *modals.NAME_INPUT
    )

    is_valid = modals.driver.execute_script(
        "return arguments[0].checkValidity()",
        name,
    )

    assert not is_valid


@allure.feature("Modals")
@allure.title("Некорректный email не проходит валидацию")
def test_invalid_email_fails_validation(modals):
    modals.open_form_modal()
    modals.fill_form(
        "Alex",
        "not-an-email",
        "Test message",
    )

    email = modals.driver.find_element(
        *modals.EMAIL_INPUT
    )

    is_valid = modals.driver.execute_script(
        "return arguments[0].checkValidity()",
        email,
    )

    assert not is_valid


@allure.feature("Modals")
@allure.title("Пустая форма не проходит валидацию")
def test_empty_form_fails_validation(modals):
    modals.open_form_modal()

    form = modals.driver.find_element(
        By.CSS_SELECTOR,
        ".pum-active form",
    )

    is_valid = modals.driver.execute_script(
        "return arguments[0].checkValidity()",
        form,
    )

    assert not is_valid


@allure.feature("Modals")
@allure.title("После закрытия формы она больше не видна")
def test_closed_form_is_not_visible(modals):
    modals.open_form_modal()
    modals.close_modal()

    assert not modals.is_modal_open()
