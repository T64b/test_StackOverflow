from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import time


# Base class for Page Object
class Base:
    def __init__(self, driver):
        self.driver = driver.driver

    def element(self, locator):
        wait = WebDriverWait(self.driver, 2)
        elem = wait.until(lambda x: x.find_element_by_xpath(locator))
        web_elem = wait.until(ec.visibility_of(elem))
        while True:
            if web_elem.is_enabled() and web_elem.is_displayed():
                return web_elem
            time.sleep(0.1)

    def elements(self, locator):
        wait = WebDriverWait(self.driver, 2)
        elem = wait.until(lambda x: x.find_elements_by_xpath(locator))
        return elem


# Fixtures class
class Fixture:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(5)

    def destroy(self):
        self.driver.quit()
