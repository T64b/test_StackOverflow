from page_objects import main_page


def test_get_title(browser):
    browser.driver.get('https://stackoverflow.com')
    page = main_page.MainPage(browser)
    assert "Stack Overflow " in page.get_title()


def test_logging(browser):
    browser.driver.get('https://stackoverflow.com')
    page = main_page.MainPage(browser)
    log_page = page.press_log_in()
    logged_user_page = log_page.logging()
    assert "Log In - Stack Overflow" in logged_user_page.get_title()


def test_search_on_site(browser):
    browser.driver.get('https://stackoverflow.com')
    page = main_page.MainPage(browser)
    result_txt = page.search_smthng('python')
    assert "Python is a multi-paradigm" in result_txt


def test_ask_question(browser):
    browser.driver.get('https://stackoverflow.com')
    page = main_page.MainPage(browser)
    log_page = page.press_log_in()
    log_page.logging()
    ask_page = page.press_ask_btn()
    result = ask_page.tag_send_text('python')
    assert "python" in result
