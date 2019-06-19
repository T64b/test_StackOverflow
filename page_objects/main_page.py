from helpers import web_element
from page_objects import log_in_page
from page_objects import ask_question_page
from selenium.webdriver.common.keys import Keys


class MainPage(web_element.Base):

    # Locators

    search_field = "//input[@name='q']"
    log_in_btn = "//a[text()='Log in']"
    text_p = "//div[@class='mb24']/p"
    ask_question_btn = "//a[@href='/questions/ask']"

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.driver.title

    def press_log_in(self):
        log_btn = self.element(self.log_in_btn)
        log_btn.click()
        return log_in_page.LogInPage(self)

    def search_smthng(self, text):
        srch_fld = self.element(self.search_field)
        srch_fld.send_keys(text)
        srch_fld.send_keys(Keys.ENTER)
        sm_txt = self.element(self.text_p)
        return sm_txt.text

    def press_ask_btn(self):
        ask_btn = self.element(self.ask_question_btn)
        ask_btn.click()
        return ask_question_page.AskQuestion(self)