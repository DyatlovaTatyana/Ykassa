from selenium.webdriver.common.by import By
from base_page import BasePage


class OrderStatusPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для статуса заказа
    def order_status_locator(self):
        return By.XPATH, "//h3/span[@class='green']"

    # Метод для проверки статуса заказа
    def check_order_status(self):
        try:
            # Ожидание появления элемента со статусом заказа
            order_status_element = self.find_element(self.order_status_locator(), time=5)
            # Проверка, что текст элемента соответствует "Принят"
            return order_status_element.text.strip() == "Принят"
        except Exception as e:
            print(f"Error while checking order status: {e}")
            return False