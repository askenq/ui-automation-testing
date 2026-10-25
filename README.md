# UI Automation Testing Project

## Описание проекта

Проект предназначен для автоматического тестирования веб-страниц с помощью Selenium и Pytest.

Основные страницы сайта Practice Automation:

- **Calendars** — проверка поля даты и валидации введённых значений.
- **Modals** — проверка открытия и закрытия модальных окон, заполнения формы и валидации.
- **Ads** — проверка появления и закрытия рекламного окна.

Дополнительно проверяется страница Form Fields: Selenium получает список инструментов из раздела Automation Tools и заполняет им поле Message.

## Используемые технологии

- Python 3.12
- Selenium WebDriver
- Pytest
- Allure Reports
- Google Chrome

## Структура проекта

```text
olimp/
├── pages/
│   ├── __init__.py
│   ├── ads_page.py
│   ├── calendars_page.py
│   ├── form_fields_page.py
│   └── modals_page.py
├── tests/
│   ├── __init__.py
│   ├── test_ads.py
│   ├── test_calendars.py
│   ├── test_form_fields.py
│   ├── test_modals.py
│   ├── test_pages_smoke.py
│   └── test_setup.py
├── utils/
│   ├── __init__.py
│   ├── check_calendar_submit.py
│   └── inspect_pages.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Установка

1. Установите Python 3.12 и Google Chrome.
2. Клонируйте репозиторий или скачайте проект.
3. Создайте виртуальное окружение:

   ```powershell
   python -m venv .venv
   ```

4. Активируйте окружение:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Установите зависимости:

   ```powershell
   pip install -r requirements.txt
   ```

## Запуск тестов

Запуск всех тестов:

```powershell
python -m pytest -v
```

Запуск тестов отдельных страниц:

```powershell
python -m pytest tests/test_calendars.py -v
python -m pytest tests/test_modals.py -v
python -m pytest tests/test_ads.py -v
python -m pytest tests/test_form_fields.py -v
```

## Allure-отчёт

Запустите тесты с сохранением результатов:

```powershell
python -m pytest --alluredir=allure-results
```

Создайте HTML-отчёт:

```powershell
allure generate allure-results --clean -o allure-report
```

Откройте отчёт:

```powershell
allure open allure-report
```

Для работы Allure CLI необходима установленная Java.

## Результаты тестирования

Последний полный запуск Pytest: **39 passed**.

Все тесты завершились успешно. Для просмотра подробных результатов используйте Allure-отчёт.

## Архитектура

В проекте используется Page Object Model (POM). Классы для взаимодействия со страницами находятся в каталоге `pages`, а автоматические тесты — в каталоге `tests`.

Общие настройки Selenium, фикстура браузера и прикрепление скриншотов при ошибках находятся в `conftest.py`.