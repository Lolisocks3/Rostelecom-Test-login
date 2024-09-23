Этот репозиторий содержит набор автоматизированных тестов для проверки функциональности входа пользователя с использованием Selenium WebDriver и фреймворка Pytest. 
Тесты охватывают как валидные, так и невалидные сценарии входа с использованием различных типов учетных данных, таких как номер телефона, электронная почта, имя пользователя и лицевой счет.

Единственная нереализированная функция - это ввод капчи, т.к это невозможно сделать с помощью каких либо алгоритмов

Использованные инструменты:
Python v. 3.12.4, Pytest v. 7.4.4, Selenium v. 4.24.0, DevTools
Selenium использовался для автоматизации работы с интерфейсом сайта
DevTools Использовался с целью определения и указания элементов для Selenium

Ссылка на тест-кейсы: https://docs.google.com/spreadsheets/d/1A7pBS_TdC7Xoakiap1vinb1xonpg5PX7ySK879ewx3A/edit?usp=sharing

1) Установите необходимые Python-пакеты: pip install -r requirements.txt

2) Введите тестовые данные в файле settings

3) Запуск тестов 

Для запуска всех тестов используйте команду: pytest

Для запуска определённой категории тестов используйте команду: pytest -m (категория)

Категории тестов: valid_login - Тесты, направленные на проверку входа с валидными данными

unvalid_login - Тесты, направленные на проверку входа с НЕвалидными данными

pass_recovery - Тесты, направленные на проверку восстановления пароля

unvalid_pass_recovery - Тесты, направленные на проверку восстановления пароля с НЕвалидными значениями

reg - Тесты, направленные на проверку регистрации

unvalid_reg - Тесты, направленные на проверку регистрации с НЕвалидными данными
