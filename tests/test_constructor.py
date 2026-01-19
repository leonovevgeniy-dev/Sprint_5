import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
from curl import MAIN_SITE, LOGIN_PAGE
from data import TestData


class TestConstructor:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        driver.get(LOGIN_PAGE)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_SITE))
        yield
    
    def test_switch_to_buns_section(self, driver): 
        import time
        time.sleep(2)

        driver.find_element(*locators.SAUCES_SECTION).click()
        
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(locators.ACTIVE_SECTION, "Соусы")
        )
        driver.find_element(*locators.BUNS_SECTION).click()
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(locators.ACTIVE_SECTION, "Булки")
        )
        
        active_section = driver.find_element(*locators.ACTIVE_SECTION)
        assert "Булки" in active_section.text
    
    def test_switch_to_sauces_section(self, driver):
        
        driver.find_element(*locators.SAUCES_SECTION).click()
        
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(locators.ACTIVE_SECTION, "Соусы")
        )
        
        active_section = driver.find_element(*locators.ACTIVE_SECTION)
        assert "Соусы" in active_section.text
    
    def test_switch_to_fillings_section(self, driver):
        driver.find_element(*locators.FILLINGS_SECTION).click()
        
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(locators.ACTIVE_SECTION, "Начинки")
        )
        
        active_section = driver.find_element(*locators.ACTIVE_SECTION)
        assert "Начинки" in active_section.text