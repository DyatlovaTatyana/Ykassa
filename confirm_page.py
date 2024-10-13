from selenium.webdriver.common.by import By
from base_page import BasePage


class ConfirmPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для кнопки оформить заказ"
    def button_confirm_locator(self):
        return By.XPATH, f'//button[@id="create_order"]'

    # Локатор для ввода контактного телефона"
    def input_for_phone_locator(self):
        return By.XPATH, f'//input[@id="client_phone"]'

    # Локатор для ввода населенного пункта"
    def input_for_address_locator(self):
        return By.XPATH, f'//input[@id="shipping_address_full_locality_name"]'

    # Локатор для водда контактного лица"
    def input_for_contact_locator(self):
        return By.XPATH, f'//input[@id="client_name"]'

    # Локатор для чекбокса курьер"
    def checkbox_courier_locator(self):
        return By.XPATH, f'//label[@for="order_delivery_variant_id_7870784"]//span[@class="radio co-delivery_method-input co-toggable_field-input co-toggable_field-input--radio"]'

    # Локатор для чекбокса юкасса"
    def checkbox_ykassa_locator(self):
        return By.XPATH, f'//label[@for="order_payment_gateway_id_1412943"]//span[@class="co-payment_method-input co-toggable_field-input  co-toggable_field-input--radio"]'


    #Локатор для текста "Поле не заполнено"
    def error_message_locator2(self):
        return By.XPATH, f'//*[@id="tabs-person"]/div[1]/div'


    # Метод для проверки видимости сообщения "поле не заполнено"
    def is_text_error(self):
        error_message = self.find_element(self.error_message_locator2())
        text = error_message.text
        return text

    #Метод для клика по "оформить заказ"
    def clic_to_button_confirm(self):
        self.find_element(self.button_confirm_locator())
        self.click(self.button_confirm_locator())

    # Метод для получения текста из поля адреса
    def get_address_value(self):
        return self.find_element(self.input_for_address_locator()).get_attribute('value')

    #Метод для заполнения всех обяазтельных полей
    def enter_required_data(self):
        self.send_keys(self.input_for_phone_locator(), "89268865997")
        self.send_keys(self.input_for_address_locator(), "Москва")
        self.send_keys(self.input_for_contact_locator(), "Дятлова Татьяна")

    #Метод для выбора чекбокса курьером
    def clic_to_checkbox_courier(self):
        self.find_element(self.checkbox_courier_locator())
        self.click(self.checkbox_courier_locator())

    #Метод для выбора чекбокса юкасса
    def clic_to_checkbox_Ykassa(self):
        self.find_element(self.checkbox_ykassa_locator())
        self.click(self.checkbox_ykassa_locator())