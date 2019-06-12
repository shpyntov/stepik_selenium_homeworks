from selenium import webdriver
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element_by_name('firstname').send_keys('Ivan')
browser.find_element_by_name('lastname').send_keys('Ivanov')
browser.find_element_by_name('email').send_keys('ivan@mail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

browser.find_element_by_name('file').send_keys(file_path)
browser.find_element_by_class_name('btn').click()
