import pytest
from selenium import webdriver
import time
import math
final = ''

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(final)

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
class TestLogin(object):

    def test_guest_should_see_login_link(self, browser, links):
        global final
        answer: float = math.log(int(time.time()))
        link = f"{links}"
        browser.get(link)
        time.sleep(5)
        button2 = browser.find_element_by_css_selector(".string-quiz__textarea")
        print(button2)
        button2.send_keys(str(answer))
        time.sleep(1)
        button = browser.find_element_by_css_selector(".submit-submission")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_css_selector(".smart-hints__feedback").text
        time.sleep(1)
        print(welcome_text_elt)

        try:
            assert 'Correct!' == welcome_text_elt
        except AssertionError:
            final += welcome_text_elt  # собираем ответ про Сов с каждой ошибкой

        browser.quit
