from selenium import webdriver
import os
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

browser.find_element_by_name("firstname").send_keys("Name")
browser.find_element_by_name("lastname").send_keys("lastname")
browser.find_element_by_name("email").send_keys("email")

current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
file_path = os.path.join(current_dir, 'file.txt')
print(file_path)
browser.find_element_by_css_selector("#file").send_keys(file_path)

browser.find_element_by_css_selector(".btn-primary").click()
