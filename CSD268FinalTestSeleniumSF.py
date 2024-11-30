# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCase1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case1(self):
        driver = self.driver
        driver.get("https://letsusedata.com/index.html")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Theme'])[1]/following::div[3]").click()
        driver.find_element_by_id("txtUser").clear()
        driver.find_element_by_id("txtUser").send_keys("test1")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Theme'])[1]/following::div[3]").click()
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("Test12456")
        driver.find_element_by_id("javascriptLogin").click()
        driver.get("https://letsusedata.com/CourseSelection.html")

    def test_case2(self):
        driver = self.driver
        driver.get("https://letsusedata.com/index.html")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Theme'])[1]/following::div[3]").click()
        driver.find_element_by_id("txtUser").clear()
        driver.find_element_by_id("txtUser").send_keys("test1")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Theme'])[1]/following::div[3]").click()
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("test1234")
        driver.find_element_by_id("javascriptLogin").click()
        self.assertEqual("Password was incorrect", driver.find_element_by_id("lblMessage").text)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
