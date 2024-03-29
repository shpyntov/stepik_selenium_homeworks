from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

x = browser.find_element_by_id('treasure').get_attribute('valuex')
y = calc(x)

browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
