from selenium import webdriver

browser = webdriver.Chrome()
# выход из всплыывашки с одним ок.
alert = browser.switch_to.alert
alert.accept()
# Взять текст из всплывашки
alert = browser.switch_to.alert
alert_text = alert.text
# Подтвержить сплывашку с выбором
confirm = browser.switch_to.alert
confirm.accept()
# отклонить всплывашку с выбором
confirm.dismiss()
# Ввод в всплывашку текста
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
