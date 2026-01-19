import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
from curl import MAIN_SITE, LOGIN_PAGE, PROFILE_PAGE
from data import TestData


class TestLogout:
    
    def test_logout_from_personal_account(self, driver): 
        driver.get(LOGIN_PAGE)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_SITE))
        
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_PAGE))
        
        driver.find_element(*locators.LOGOUT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_PAGE))
        assert driver.current_url == LOGIN_PAGE