from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.CSS_SELECTOR, '.btn[name="registration_submit"]')

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_BSKT = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_BSKT = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > .btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_STATE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
