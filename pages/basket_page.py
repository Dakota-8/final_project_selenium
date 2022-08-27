from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty"

    def should_be_empty_text(self):
        message = self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE)  # if message about empty is true ->
        if message:
            self.should_be_message_basket_is_empty()

    def should_be_message_basket_is_empty(self):
        languages = {
            "ar": "سلة التسوق فارغة متابعة التسوق",
            "ca": "La seva cistella està buida. Continua les seves compres",
            "cs": "Váš košík je prázdný. Pokračovat v nakupování",
            "da": "Din indkøbskurv er tom. Køb mere",
            "de": "Ihr Warenkorb ist leer. Einkauf fortsetzen",
            "en-gb": "Your basket is empty. Continue shopping",
            "el": "Το καλάθι σας είναι άδειο. Συνεχίστε τις αγορές σας",
            "es": "Tu carrito esta vacío. Continuar sus compras",
            "fi": "Korisi on tyhjä Jatka ostoksia",
            "fr": "Korisi on tyhjä Jatka ostoksia",
            "it": "Il tuo carrello è vuoto. Continua lo shopping",
            "ko": "장바구니가 비었습니다. 쇼핑 계속하기",
            "nl": "Je winkelmand is leeg Verdergaan met winkelen",
            "pl": "Twój koszyk jest pusty. Kontynuuj zakupy",
            "pt": "O carrinho está vazio. Continuar a comprar",
            "pt-br": "Sua cesta está vazia. Continuar comprando",
            "ro": "Cosul tau este gol. Continua cumparaturile",
            "ru": "Ваша корзина пуста Продолжить покупки",
            "sk": "Váš košík je prázdny Pokračovať v nákupe",
            "uk": "Ваш кошик пустий. Продовжити покупки",
            "zh-hans": "Your basket is empty. Continue shopping",
        }
        assert self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text in languages.values(), \
            "Basket is not empty"
