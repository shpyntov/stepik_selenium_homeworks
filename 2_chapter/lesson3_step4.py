from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

browser.find_element_by_class_name('btn').click()
browser.switch_to.alert.accept()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

browser.find_element_by_id('answer').send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()
