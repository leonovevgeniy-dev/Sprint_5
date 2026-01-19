import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
from curl import MAIN_SITE, LOGIN_PAGE, REGISTER_PAGE, FORGOT_PASSWORD_PAGE
from data import TestData


class TestLogin:
    
    def test_login_from_main_page_button(self, driver, wait):
        """
        Проверка входа по кнопке «Войти в аккаунт» на главной.
        """ 
        driver.find_element(*locators.LOGIN_BUTTON_MAIN).click()
        assert driver.current_url == LOGIN_PAGE
        driver.find_element(*locators.EMAIL_INPUT).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
        
        wait.until(EC.url_to_be(MAIN_SITE))
        assert driver.current_url == MAIN_SITE
    
    def test_login_from_personal_account_button(self, driver, wait):
        """
        Проверка входа через кнопку «Личный кабинет».
        """ 
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == LOGIN_PAGE  
        driver.find_element(*locators.EMAIL_INPUT).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
        
        wait.until(EC.url_to_be(MAIN_SITE))
        assert driver.current_url == MAIN_SITE
    
    def test_login_from_register_page_link(self, driver, wait):
        """
        Проверка входа через кнопку в форме регистрации.
        """
        driver.get(REGISTER_PAGE)
        driver.find_element(*locators.REGISTER_LOGIN_LINK).click()
        assert driver.current_url == LOGIN_PAGE
        driver.find_element(*locators.EMAIL_INPUT).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
        
        wait.until(EC.url_to_be(MAIN_SITE))
        assert driver.current_url == MAIN_SITE
    
    def test_login_from_forgot_password_page_link(self, driver, wait):
        """
        Проверка входа через кнопку в форме восстановления пароля.
        """
        driver.get(FORGOT_PASSWORD_PAGE)
        driver.find_element(*locators.FORGOT_LOGIN_LINK).click()
        assert driver.current_url == LOGIN_PAGE
        driver.find_element(*locators.EMAIL_INPUT).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
        
        wait.until(EC.url_to_be(MAIN_SITE))
        assert driver.current_url == MAIN_SITE