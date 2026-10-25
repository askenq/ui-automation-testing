
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.calendars_page import CalendarsPage


INVALID_MESSAGE = "Please enter a valid date."


@pytest.fixture
def calendar(driver):
    return CalendarsPage(driver).open()


@allure.feature("Calendars")
@allure.title("Страница календаря открывается")
def test_calendar_page_opens(calendar):
    assert "Calendars" in calendar.driver.title


@allure.feature("Calendars")
@allure.title("Поле даты отображается")
def test_date_field_is_visible(calendar):
    field = calendar.driver.find_element(*calendar.DATE_INPUT)
    assert field.is_displayed()


@allure.feature("Calendars")
@allure.title("Кнопка отправки доступна")
def test_submit_button_enabled(calendar):
    button = calendar.driver.find_element(*calendar.SUBMIT_BUTTON)
    assert button.is_displayed()
    assert button.is_enabled()


@pytest.mark.parametrize(
    "date_value",
    [
        "2026-10-25",
        "2026-01-01",
        "2024-02-29",
        "2027-12-31",
    ],
)
@allure.feature("Calendars")
@allure.title("Корректная дата принимается: {date_value}")
def test_valid_date_submission(calendar, date_value):
    calendar.enter_date(date_value)
    calendar.submit()

    WebDriverWait(calendar.driver, 5).until(
        lambda d: calendar.get_date_value() == date_value
    )

    body = calendar.driver.find_element(By.TAG_NAME, "body").text
    assert INVALID_MESSAGE not in body
    assert calendar.get_date_value() == date_value


@allure.feature("Calendars")
@allure.title("Поле даты можно очистить")
def test_clear_date(calendar):
    calendar.enter_date("2026-10-25")
    calendar.enter_date("")

    assert calendar.get_date_value() == ""


@pytest.mark.parametrize(
    "invalid_date",
    [
        "not-a-date",
        "2026-02-30",
        "25/10/2026",
    ],
)
@allure.feature("Calendars")
@allure.title("Некорректная дата отклоняется: {invalid_date}")
def test_invalid_date_is_rejected(calendar, invalid_date):
    calendar.enter_date(invalid_date)
    calendar.submit()

    error = WebDriverWait(calendar.driver, 5).until(
        lambda d: next(
            (
                element
                for element in d.find_elements(
                    By.XPATH,
                    "//*[contains(normalize-space(.), "
                    "'Please enter a valid date.')]",
                )
                if element.is_displayed()
                and element.text.strip() == INVALID_MESSAGE
            ),
            False,
        )
    )

    assert error is not False
