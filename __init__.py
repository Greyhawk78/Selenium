import time

from selenium.webdriver.common.by import By
import time


def test_check_button_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    assert browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/button'), 'Button not found'