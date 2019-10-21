from math import sin, log
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/redirect_accept.html")

driver.find_element_by_css_selector(".trollface").click()
# Показывает окна и переключает их
string = driver.window_handles
print(string)
driver.switch_to.window(string[1])

test = driver.find_element_by_css_selector("#input_value").text
test = int(test)
fun = log(abs(12*sin(test)))
print(fun)
driver.find_element_by_id("answer").send_keys(str(fun))
driver.find_element_by_css_selector(".btn-primary").click()
