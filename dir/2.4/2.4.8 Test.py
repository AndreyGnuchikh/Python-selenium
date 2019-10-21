import time
from cmath import sin
from math import log

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
# Не только кликабельность можно проверять
        EC.text_to_be_present_in_element(
            (By.ID, "price"), "$100")
    )
browser.find_element_by_id("book").click()
time.sleep(1)
test = browser.find_element_by_css_selector("#input_value").text
test = int(test)
print(test)
fun = log(abs(12*sin(test)))
print(fun)
browser.find_element_by_id("answer").send_keys(str(fun))
browser.find_element_by_css_selector("#solve").click()
