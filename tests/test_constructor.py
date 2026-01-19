import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import locators


class TestConstructor:
    
    @pytest.mark.parametrize("section_to_test,expected_text", [
        (locators.SAUCES_SECTION, "Соусы"),
        (locators.FILLINGS_SECTION, "Начинки"),
        (locators.BUNS_SECTION, "Булки"),
    ])
    def test_switch_to_section(self, login, wait, section_to_test, expected_text):
       
        driver = login
        actions = ActionChains(driver)
        
        element = wait.until(EC.element_to_be_clickable(section_to_test))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        actions.move_to_element(element).pause(0.5).click().perform()
        
        wait.until(EC.text_to_be_present_in_element(locators.ACTIVE_SECTION, expected_text))
        
        active_section = driver.find_element(*locators.ACTIVE_SECTION)
        assert expected_text in active_section.text