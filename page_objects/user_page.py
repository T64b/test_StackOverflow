from helpers import web_element


class LoggedUserPage(web_element.Base):

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.driver.title

