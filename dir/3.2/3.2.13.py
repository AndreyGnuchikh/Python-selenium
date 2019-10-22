import unittest
from datetime import time

from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestAbs(unittest.TestCase):

    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        ...

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get(link2)

        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.third_class > input")
        input2.send_keys("123")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt2 = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text2 = welcome_text_elt2.text
        self.assertEqual(welcome_text2, "Congratulation2s! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
