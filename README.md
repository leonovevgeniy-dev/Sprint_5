# Sprint 5: Автотесты для Stellar Burgers

Автоматизированные тесты для веб-приложения Stellar Burgers.


Технологии
Python 3.8+
Selenium 4
Pytest
Faker

# Структура проекта
Sprint_5/
conftest.py # Фикстуры
curl.py # URL приложения
data.py # Тестовые данные
locators.py # Локаторы элементов
helper.py # Генераторы данных

tests/ # 13 тестов
test_registration.py # 2 теста
test_login.py # 4 теста
test_navigation.py # 3 теста
test_logout.py # 1 тест
test_constructor.py # 3 теста

requirements.txt # Зависимости
.gitignore # Игнорируемые файлы


Установка
```bash
pip install -r requirements.txt

Запуск тестов
bash
pytest
