from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_BUTTON), "Add to basket button isn't presented"

    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()

    def should_item_in_basket(self):
        self.should_cost_equal()
        self.should_name_equal()

    def should_cost_equal(self):
        item_basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        item_product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert item_product_cost == item_basket_cost, 'Prices not equal'

    def should_name_equal(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_add_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET).text
        assert product_name == product_add_name, "Names of product isn't equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"
