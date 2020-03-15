from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items are presented"

    def check_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_STATE), "Empty basket text is not presented"
