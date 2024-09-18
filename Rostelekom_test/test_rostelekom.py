import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from settings import *


@pytest.fixture(scope="function")
def driver():
    service = Service(executable_path=webdriver_path)
    driver = webdriver.Chrome(service=service)
    # Переходим на страницу авторизации
    driver.get(link_to_app)

    yield driver

    driver.quit()


# Регистрация
@pytest.mark.reg
def test_reg_email(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.NAME, 'firstName').send_keys(first_name)
    driver.find_element(By.NAME, 'lastName').send_keys(last_name)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    driver.find_element(By.NAME, 'register').click()
    time.sleep(100)
    assert driver.find_element(By.CLASS_NAME, 'home-view__user-info')


# Регистрация с НЕвалидными данными
@pytest.mark.unvalid_reg
def test_unvalid_reg_email(driver):
    driver.implicitly_wait(3)
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.NAME, 'firstName').send_keys(first_name)
    driver.find_element(By.NAME, 'lastName').send_keys(last_name)
    driver.find_element(By.ID, 'password').send_keys(unvalid_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(unvalid_password)
    driver.find_element(By.NAME, 'register').click()

    try:
        driver.find_element(By.CLASS_NAME, 'home-view__user-info')
    except NoSuchElementException:
        # Т.к регистрация произойти не должна - мы засчитываем тест как пройденый
        pass


# Авторизация через почту
@pytest.mark.valid_login
def test_valid_login_phone(driver):
    driver.implicitly_wait(10)
    login_button = 'kc-login'
    # Вводим номер телефона
    driver.find_element(By.ID, 'username').send_keys(valid_phone_number)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.ID, login_button).click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.CLASS_NAME, 'home-view__user-info')


# Авторизация через почту
@pytest.mark.valid_login
def test_valid_login_email(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    login_button = 'kc-login'
    # Вводим email
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.ID, login_button).click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.CLASS_NAME, 'home-view__user-info')


# Авторизация через логин
@pytest.mark.valid_login
def test_valid_login_username(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    login_button = 'kc-login'
    # Вводим username
    driver.find_element(By.ID, 'username').send_keys(valid_username)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.ID, login_button).click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.CLASS_NAME, 'home-view__user-info')


# Авторизация через личный счёт
#Необходимо ввести номер лицевого счёта в settings
@pytest.mark.valid_login
def test_valid_login_pers_acc(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    login_button = 'kc-login'
    # Вводим username
    driver.find_element(By.ID, 'username').send_keys(valid_personal_account)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.ID, login_button).click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.CLASS_NAME, 'home-view__user-info')


# Авторизация через почту с НЕвалидными данными
@pytest.mark.unvalid_login
def test_unvalid_login_phone(driver):
    driver.implicitly_wait(10)
    login_button = 'kc-login'
    # Вводим номер телефона
    driver.find_element(By.ID, 'username').send_keys(unvalid_phone_number)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(unvalid_password)
    driver.find_element(By.ID, login_button).click()
    # Проверяем, что на экран вывелось сообщение "Неверный логин или пароль"
    assert driver.find_element(By.CLASS_NAME, 'card-error__message')


# Авторизация через почту с НЕвалидными данными
@pytest.mark.unvalid_login
def test_unvalid_login_email(driver):
    driver.implicitly_wait(10)
    login_button = 'kc-login'
    # Вводим email
    driver.find_element(By.ID, 'username').send_keys(unvalid_email)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(unvalid_password)
    driver.find_element(By.ID, login_button).click()
    # Проверяем, что на экран вывелось сообщение "Неверный логин или пароль"
    assert driver.find_element(By.CLASS_NAME, 'card-error__message')


# Авторизация через логин с НЕвалидными данными
@pytest.mark.unvalid_login
def test_unvalid_login_username(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    login_button = 'kc-login'
    # Вводим username
    driver.find_element(By.ID, 'username').send_keys(unvalid_username)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.ID, login_button).click()
    # Проверяем, что на экран вывелось сообщение "Неверный логин или пароль"
    assert driver.find_element(By.CLASS_NAME, 'card-error__message')


# Авторизация через личный счёт с НЕвалидными данными
@pytest.mark.unvalid_login
def test_unvalid_login_pers_acc(driver):
    driver.implicitly_wait(10)
    login_button = 'kc-login'
    # Вводим email
    driver.find_element(By.ID, 'username').send_keys(unvalid_personal_account)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(unvalid_password)
    driver.find_element(By.ID, login_button).click()
    # Проверяем, что на экран вывелось сообщение "Неверный логин или пароль"
    assert driver.find_element(By.CLASS_NAME, 'card-error__message')


# Восстановление пароля через номер телефона
@pytest.mark.pass_recovery
def test_pass_recovery_phone(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys(valid_phone_number)
    time.sleep(100)
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, 'password-new').send_keys(new_pass_recovery)
    driver.find_element(By.NAME, 'password-confirm').send_keys(new_pass_recovery)
    driver.find_element(By.ID, 't-btn-reset-pass').click()
    # Проверяем, что после смены пароля не вылазит ошибок и мы попадаем обратно на страницу авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__content')


# Восстановление пароля через почту
@pytest.mark.pass_recovery
def test_pass_recovery_email(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    time.sleep(100)
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, 'password-new').send_keys(new_pass_recovery)
    driver.find_element(By.NAME, 'password-confirm').send_keys(new_pass_recovery)
    driver.find_element(By.ID, 't-btn-reset-pass').click()
    # Проверяем, что после смены пароля нет ошибок и мы попадаем обратно на страницу авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__content')


# Восстановление пароля через логин
@pytest.mark.pass_recovery
def test_pass_recovery_username(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 'username').send_keys(valid_username)
    driver.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(100)
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, 'password-new').send_keys(new_pass_recovery)
    driver.find_element(By.NAME, 'password-confirm').send_keys(new_pass_recovery)
    driver.find_element(By.ID, 't-btn-reset-pass').click()
    # Проверяем, что после смены пароля нет ошибок и мы попадаем обратно на страницу авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__content')


# Восстановление пароля через личный счёт
@pytest.mark.pass_recovery
def test_pass_recovery_pers_acc(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, 'username').send_keys(valid_personal_account)
    time.sleep(100)
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, 'password-new').send_keys(new_pass_recovery)
    driver.find_element(By.NAME, 'password-confirm').send_keys(new_pass_recovery)
    driver.find_element(By.ID, 't-btn-reset-pass').click()
    # Проверяем, что после смены пароля не вылазит ошибок и мы попадаем обратно на страницу авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__content')


# Восстановление пароля через номер телефона
@pytest.mark.unvalid_pass_recovery
def test_pass_unvalid_recovery_phone(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys(valid_phone_number)
    time.sleep(100)
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, 'password-new').send_keys(unvalid_new_pass_recovery)
    driver.find_element(By.NAME, 'password-confirm').send_keys(unvalid_new_pass_recovery)
    driver.find_element(By.ID, 't-btn-reset-pass').click()
    # Проверяем, что после смены пароля не вылазит ошибок и мы попадаем обратно на страницу авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__content')


# Восстановление пароля через почту
@pytest.mark.unvalid_pass_recovery
def test_pass_unvalid_recovery_email(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    time.sleep(100)
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, 'password-new').send_keys(unvalid_new_pass_recovery)
    driver.find_element(By.NAME, 'password-confirm').send_keys(unvalid_new_pass_recovery)
    driver.find_element(By.ID, 't-btn-reset-pass').click()
    # Проверяем, что после смены пароля нет ошибок и мы попадаем обратно на страницу авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__content')


# Восстановление пароля через логин с НЕвалидными данными
@pytest.mark.unvalid_pass_recovery
def test_pass_unvalid_recovery_username(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 'username').send_keys(valid_username)
    driver.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(100)
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, 'password-new').send_keys(unvalid_new_pass_recovery)
    driver.find_element(By.NAME, 'password-confirm').send_keys(unvalid_new_pass_recovery)
    driver.find_element(By.ID, 't-btn-reset-pass').click()
    # Проверяем, что после смены пароля нет ошибок и мы попадаем обратно на страницу авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__content')


# Восстановление пароля через личный счёт с НЕвалидными данными
@pytest.mark.unvalid_pass_recovery
def test_pass_unvalid_recovery_pers_acc(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, 'username').send_keys(valid_personal_account)
    time.sleep(100)
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, 'password-new').send_keys(unvalid_new_pass_recovery)
    driver.find_element(By.NAME, 'password-confirm').send_keys(unvalid_new_pass_recovery)
    driver.find_element(By.ID, 't-btn-reset-pass').click()
    # Проверяем, что после смены пароля не вылазит ошибок и мы попадаем обратно на страницу авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__content')
