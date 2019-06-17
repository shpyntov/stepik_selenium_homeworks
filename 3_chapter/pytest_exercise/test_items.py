import time

def test_basket_button_visible(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.find_element_by_class_name("btn-add-to-basket").is_displayed()
    # time.sleep(30)
