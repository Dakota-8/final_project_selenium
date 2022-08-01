from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FROM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div>h1 + p')
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, '.alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1)')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
