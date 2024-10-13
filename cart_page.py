from xmlrpc.client import Boolean

from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для поиска товара по data-product-id
    def product_form_cartpage_locator(self, product_id):
        return By.XPATH, f'//form[@data-product-id="{product_id}"]//div[@class="product-preview__content"]'

    # Локатор для кнопки "В корзину" внутри формы продукта
    def add_to_cart_button_cartpage_locator(self, product_id):
        return (
            By.XPATH,
            f'//form[@data-product-id="{product_id}"]//div[@class="product-preview__content"]//button[@class="button add-cart-counter__btn"]')

    #Локатор для кнопки "Оформить заказ"
    def place_an_order_button_locator(self):
        return By.XPATH, f'//button[@class= "button button_size-l button_wide"]'

    # Локатор для кнопки "удалить"
    def trach_button_locarot(self,product_id):
        return By.XPATH, f'//div[@data-product-id="{product_id}"]//button[@class="button js-item-delete icon icon-trash"]'

    # Локатор для формы товара
    def cart_item_locator(self, product_id):
        return By.XPATH, f'//div[@data-product-id="{product_id}"]'

    # Локатор для формы заказа справо
    def form_order_locator1(self):
        return By.XPATH, f'//div[@class="cart__area-controls-sticky"]'

    #Локатор для поля ввода промокода
    def input_promo_locator(self):
        return By.XPATH, f'//input[@name="cart[coupon]"]'

    # Локатор для применения промокода
    def button_promo_locator(self):
        return By.XPATH, f"//button[@class='coupon-button button button-link_size-m']"

    #Локатор для сообщения "введен несущ промокод"
    def text_promo_locator(self):
        return By.XPATH, "//div[@class='cart__area-coupon']//div[@class='insales-ui-discount-error']"


    #Метод для проверки видимости текста
    def form_order_locator(self):
        return self.find_element(self.form_order_locator1())

    # Метод для проверки видимости сообщения "введен несущ промокод"
    def text_promo(self):
        error_message = self.find_element(self.text_promo_locator())
        text = error_message.text
        return text

    #Метод для клика по кнопке промокода
    def clic_to_button_promo(self):
        self.find_element(self.button_promo_locator())
        self.click(self.button_promo_locator())

    # Метод для ввода значения в поле промокода
    def input_promo(self):
        self.send_keys(self.input_promo_locator(),"я люблю автотетсы")

    # Метод для клика по иконке урны
    def clic_to_icon_trash(self,product_id):
        # Найти иконку урны
        self.find_element(self.trach_button_locarot(product_id))
        # Кликнуть по иконке
        self.click(self.trach_button_locarot(product_id))

    # Метод для клика по оформить заказ
    def clic_to_button_confirm(self):
        # Найти кнопку
        self.find_element(self.place_an_order_button_locator())
        # Кликнуть по кнопке
        self.click(self.place_an_order_button_locator())



