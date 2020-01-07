import pytest
from selenium import webdriver

def test_guest_should_see_login_link(browser, language):
    link = "http://selenium1py.pythonanywhere.com/{}/".format(language)
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")