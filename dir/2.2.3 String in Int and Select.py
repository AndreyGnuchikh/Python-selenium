from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#num1")
    num2 = browser.find_element_by_css_selector("#num2")
    x = int(num1.text)
    y = int(num2.text)

    print(x)
    print(y)
    i: int = (x+y)
    print(i)
# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
    time.sleep(1)
    i = i.__str__()
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(i)
    browser.find_element_by_css_selector(".btn-default").click()
finally:
   browser.quit()
