from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")

# КАВЫЧКИ! можно так (что бы одни были " то другие ')
# browser.execute_script('document.title="Script executing";')
# Либо так
# browser.execute_script("document.title='Script executing';")

# Сразу нельсколько инструкций:
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
