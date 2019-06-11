from helpers import web_element


class AskQuestion(web_element.Base):

    # Locators

    radio_btn = '(//input[@name="question-type"])[1]'
    tag_field = '//input[@id="tageditor-replacing-tagnames--input"]'
    tag_srch_result = '(//span[@class="match"])[1]'

    def __init__(self, driver):
        super().__init__(driver)

    def choose_radio(self):
        radio = self.element(self.radio_btn)
        radio.click()

    def tag_send_text(self, text):
        tag = self.element(self.tag_field)
        tag.send_keys(text)
        return self.element(self.tag_srch_result).text




