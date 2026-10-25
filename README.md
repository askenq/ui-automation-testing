# UI Automation Testing Project

## Описание проекта

Проект предназначен для автоматического тестирования веб-страниц с помощью Selenium и Pytest.

Проверяются три страницы сайта Practice Automation:

- **Calendars** — работа с полем даты и проверка корректности введённых значений.
- **Modals** — открытие и закрытие модальных окон, заполнение формы и проверка валидации.
- **Ads** — появление рекламного окна, проверка его содержимого и закрытие.

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
│   └── modals_page.py
├── tests/
│   ├── __init__.py
│   ├── test_ads.py
│   ├── test_calendars.py
│   ├── test_modals.py
│   ├── test_pages_smoke.py
│   └── test_setup.py
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
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

Для запуска всех тестов выполните:

```powershell
python -m pytest -v
```

Для запуска тестов отдельной страницы:

```powershell
python -m pytest tests/test_calendars.py -v
python -m pytest tests/test_modals.py -v
python -m pytest tests/test_ads.py -v
```

## Allure-отчёт

Запуск тестов с сохранением результатов:

```powershell
python -m pytest --alluredir=allure-results
```

Создание HTML-отчёта:

```powershell
allure generate allure-results --clean -o allure-report
```

Открытие отчёта:

```powershell
allure open allure-report
```

Для работы Allure CLI необходима Java.

## Результаты тестирования

При последнем полном запуске Pytest успешно завершились 38 тестов.

Allure-отчёт подтвердил успешное выполнение всех 38 тестов.

## Архитектура

В проекте используется Page Object Model (POM). Логика взаимодействия со страницами находится в каталоге `pages`, а тесты расположены в каталоге `tests`.

Общие настройки Selenium и обработка результатов выполнения тестов находятся в `conftest.py`.
