import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
from curl import MAIN_SITE, LOGIN_PAGE, REGISTER_PAGE
from helper import generate_registration_data, generate_incorrect_password
from data import TestData


class TestRegistration:
    
    def test_successful_registration(self, driver):
        
        driver.find_element(*locators.LOGIN_BUTTON_MAIN).click()
        
        assert driver.current_url == LOGIN_PAGE
        driver.find_element(*locators.REGISTER_LINK).click()
        
        email, password = generate_registration_data()
        
        driver.find_element(*locators.NAME_INPUT).send_keys("ИванИванов")
        driver.find_element(*locators.REGISTER_EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.REGISTER_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REGISTER_BUTTON).click()
        
        wait = WebDriverWait(driver, 15) 
        wait.until(EC.url_to_be(LOGIN_PAGE))
        assert driver.current_url == LOGIN_PAGE
    
    def test_registration_with_short_password_error(self, driver): 
        
        driver.get(REGISTER_PAGE)
        
        driver.find_element(*locators.NAME_INPUT).send_keys("ИванИванов")
        driver.find_element(*locators.REGISTER_EMAIL_INPUT).send_keys("test@example.com")
        
        short_password = generate_incorrect_password() 
        driver.find_element(*locators.REGISTER_PASSWORD_INPUT).send_keys(short_password)
        
        driver.find_element(*locators.REGISTER_BUTTON).click()
        
        assert driver.current_url == REGISTER_PAGE
        
        wait = WebDriverWait(driver, 10)
        error_element = wait.until(EC.visibility_of_element_located(locators.PASSWORD_ERROR))
        
        assert error_element.text != ""