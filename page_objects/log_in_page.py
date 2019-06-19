from helpers import web_element
from page_objects import user_page
import time


class LogInPage(web_element.Base):

    # Locators

    email_field = '//input[@id="email"]'
    password_field = "//input[@id='password']"
    login = "aleksandr.bronza@gmail.com"
    password = "***********"  # if needed, please contact
    submit_btn = '//button[@id="submit-button"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.driver.title

    def logging(self):
        # import pdb;pdb.set_trace()
        email = self.element(self.email_field)
        email.clear()
        email.send_keys(self.login)
        pass_elem = self.element(self.password_field)
        pass_elem.clear()
        pass_elem.send_keys(self.password)
        time.sleep(2)
        sbm_btn = self.element(self.submit_btn)
        sbm_btn.click()
        return user_page.LoggedUserPage(self)
