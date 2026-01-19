import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import MAIN_SITE, LOGIN_PAGE
from data import TestData
import locators 

# session, module, class, function
@pytest.fixture(scope="function")
def driver(): 

    options = Options()
    options.add_argument("--window-size=1600,900")
    options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
    })
    # options.add_argument("--headless") 
    
    browser = webdriver.Chrome(options=options)
    browser.get(MAIN_SITE)
    
    yield browser
    
    browser.quit()


@pytest.fixture
def login(driver):
    driver.get(LOGIN_PAGE)
    driver.find_element(*locators.EMAIL_INPUT).send_keys(TestData.EXISTING_EMAIL)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
    driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_SITE))
    return driver

@pytest.fixture
def wait(driver): 
    return WebDriverWait(driver, 10) 

