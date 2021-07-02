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
        self.driver.get("https://calcus.ru/kalkulyator-drobej")

        elem = self.driver.find_element_by_name("n1")
        actionChains = ActionChains(self.driver)
        actionChains.double_click(elem).perform()
        elem.send_keys("5")

        elem = self.driver.find_element_by_name("d1")
        actionChains = ActionChains(self.driver)
        actionChains.double_click(elem).perform()
        elem.send_keys("5")

        elem = self.driver.find_element_by_name("n2")
        actionChains = ActionChains(self.driver)
        actionChains.double_click(elem).perform()
        elem.send_keys("5")

        elem = self.driver.find_element_by_name("d2")
        actionChains = ActionChains(self.driver)
        actionChains.double_click(elem).perform()
        elem.send_keys("5")

        elem = self.driver.find_element_by_class_name("calc-submit")
        elem.click()

        time.sleep(2)
        
        elem = self.driver.find_elements_by_css_selector ("span")
        print(elem[14].text)
        assert "2" in elem[14].text
        
    def test_2(self):
        self.driver.get("https://calcus.ru/kalkulyator-drobej")

        elem = self.driver.find_element_by_name("n1")
        actionChains = ActionChains(self.driver)
        actionChains.double_click(elem).perform()
        elem.send_keys("3")

        elem = self.driver.find_element_by_name("d1")
        actionChains = ActionChains(self.driver)
        actionChains.double_click(elem).perform()
        elem.send_keys("4")

        elem = self.driver.find_element_by_name("n2")
        actionChains = ActionChains(self.driver)
        actionChains.double_click(elem).perform()
        elem.send_keys("5")

        elem = self.driver.find_element_by_name("d2")
        actionChains = ActionChains(self.driver)
        actionChains.double_click(elem).perform()
        elem.send_keys("6")

        elem = self.driver.find_element_by_class_name("calc-submit")
        elem.click()

        time.sleep(2)
        

        num = self.driver.find_element_by_xpath("//div[@class='float-left calc-result-value result-placeholder-fraction']/div[1]/span[1]")
        n3 = self.driver.find_element_by_xpath("//div[@class='float-left calc-result-value result-placeholder-fraction']/div[2]/div[1]")
        d3 = self.driver.find_element_by_xpath("//div[@class='float-left calc-result-value result-placeholder-fraction']/div[2]/div[2]")


        print(num.get_attribute('innerHTML'))
        print(n3.get_attribute('innerHTML'))
        print(d3.get_attribute('innerHTML'))


        # for x in elem:
            # print(x.text)

        # print(elem[14].text)
        
        assert "1" in num.get_attribute('innerHTML')
        assert "7" in n3.get_attribute('innerHTML')
        assert "12" in d3.get_attribute('innerHTML')


if __name__ == "__main__":
    unittest.main()

