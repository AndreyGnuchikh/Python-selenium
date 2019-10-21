from math import log, sin
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://SunInJuly.github.io/execute_script.html")
idd = browser.find_element_by_id("input_value").text
idd = int(idd)
fun = log(abs(12*sin(idd)))
print(fun)
browser.find_element_by_id("answer").send_keys(str(fun))
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
browser.find_element_by_css_selector(".btn-primary").click()

