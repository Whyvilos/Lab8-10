from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_1(self):
        self.driver.get("https://vk.com/")

        elem = self.driver.find_element_by_id("index_email")
        actionChains = ActionChains(self.driver)
        actionChains.double_click(elem).perform()
        elem.send_keys("vlad03.01@mail.ru")

        elem = self.driver.find_element_by_id("index_pass")
        actionChains = ActionChains(self.driver)
        actionChains.double_click(elem).perform()
        elem.send_keys("Whyvilos031001110076R")

        elem = self.driver.find_element_by_id("index_login_button")
        elem.click()

        time.sleep(5)


        elem = self.driver.find_element_by_id("l_doc")
        elem.click()
        
        time.sleep(3)


       
        elem = self.driver.find_element_by_id("ui_rmenu_type2")
        elem.click()
        time.sleep(3)


       
        elem = self.driver.find_element_by_xpath("//div[@id='docs_file_59827757_500332139']/a[1]")
        elem.click()
        time.sleep(5)


        

if __name__ == "__main__":
    unittest.main()

