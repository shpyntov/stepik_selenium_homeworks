import pytest
from selenium import webdriver
import time
import math
from time import sleep as wait

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('page', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", '236905'])
class TestLogin(object):
    def test_page(self, browser, page):
        link = "https://stepik.org/lesson/{}/step/1".format(page)
        browser.get(link)
        answer = str(math.log(int(time.time())))
        browser.find_element_by_class_name('textarea').send_keys(answer)
        browser.find_element_by_class_name('submit-submission').click()
        text = browser.find_element_by_class_name('smart-hints__hint').text
        assert text == 'Correct!'
