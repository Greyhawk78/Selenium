from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_is_empty(self):
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text
        assert 'Your basket is empty. Continue shopping' == empty_message, f'Basket not empty, it contains {empty_message}'
