from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/execute_script.html')

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 150);")

browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
