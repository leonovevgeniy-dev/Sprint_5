import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
from curl import MAIN_SITE, LOGIN_PAGE, PROFILE_PAGE 
from data import TestData


class TestNavigation:
    
    def test_go_to_personal_account(self, driver):
 
        driver.get(LOGIN_PAGE)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_SITE))
        
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_PAGE))
        assert driver.current_url == PROFILE_PAGE
    
    def test_go_from_personal_account_to_constructor_via_button(self, driver):
      
        driver.get(LOGIN_PAGE)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_SITE))
        
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_PAGE))
        
        driver.find_element(*locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_SITE))
        assert driver.current_url == MAIN_SITE
    
    def test_go_from_personal_account_to_constructor_via_logo(self, driver):
       
        driver.get(LOGIN_PAGE)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_SITE))
        
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_PAGE))
        
        driver.find_element(*locators.LOGO_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_SITE))
        assert driver.current_url == MAIN_SITE 