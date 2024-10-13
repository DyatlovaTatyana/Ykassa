import time
import pytest
from selenium.webdriver.common.by import By
from cart_page import CartPage
from confirm_page import ConfirmPage
from start_page import StartPage
from order_page import OrderStatusPage


#ПОЗИТИВНЫЕ ТЕСТЫ
@pytest.mark.usefixtures("init_driver", "base_url")
class TestAddToCart:

    def test_add_product_to_cart(self, base_url):
        # Инициализация страницы
        start_page = StartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта, который хотим добавить в корзину
        product_id = '253355137'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)

        # Проверка, что товар добавлен в корзину
        assert start_page.is_product_added_to_cart(), "Product was not added to cart"


    def test_add_products_to_cart(self, base_url):
        # Инициализация страниц
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продуктов
        product_ids = ['253355230','253355337', '253355471']

        #Циклом добавляем продукты в корзину
        for product_id in product_ids:
            start_page.add_product_to_cart(product_id)
            assert start_page.is_product_added_to_cart(), "Product {product_id} was not added to cart"
        time.sleep(3)

        # Переходим в корзинц
        start_page.clic_to_icon_cart()

        # Проверка, что все продукты отображаются в корзине
        for product_id in product_ids:
            assert cart_page.find_element(cart_page.cart_item_locator(product_id)), (f"Product {product_id} is not "
                                                                                     f"displayed in the cart")

@pytest.mark.usefixtures("init_driver", "base_url")
class TestValueAddress:
    def test_value_address(self, base_url):
        # Инициализация страниц
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)
        confirm_page = ConfirmPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта, который хотим добавить в корзину
        product_id = '253355230'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)
        time.sleep(5)
        # Кликаем по иконке корзины
        start_page.clic_to_icon_cart()

        # Переход к оформлению заказа
        cart_page.clic_to_button_confirm()
        time.sleep(5)

        # Заполнение обязательных полей заказа
        confirm_page.enter_required_data()
        time.sleep(5)

        # Выбор курьерской доставки
        confirm_page.clic_to_checkbox_courier()

        # Выбор способа оплаты
        confirm_page.clic_to_checkbox_Ykassa()

        # Проверка, что введенный адрес валиден
        entered_address = confirm_page.get_address_value()
        assert entered_address == "г Москва", f"Expected address 'Москва', but got '{entered_address}'"

@pytest.mark.usefixtures("init_driver", "base_url")
class TestNavigate:
    def test_navigate_back_to_start_page(self, base_url):
        # Инициализация страниц
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # Кликаем по корзине
        start_page.clic_to_icon_cart()

        # Проверка, что находимся на странице корзины
        assert "cart_items" in self.driver.current_url, "Not on cart page"

        # Переход обратно на главную страницу
        start_page.open_start_page()

        # Проверка, что вернулись на главную страницу
        assert "yookassa" in self.driver.current_url, "Not on start page"


@pytest.mark.usefixtures("init_driver", "base_url")
class Order:

    def test_confirm_order(self, base_url):
        # Инициализация страниц
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)
        confirm_page = ConfirmPage(self.driver)
        order_page = OrderStatusPage(self.driver)
        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта, который хотим добавить в корзину
        product_id = '253355230'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)
        time.sleep(5)
        # Кликаем по иконке корзины
        start_page.clic_to_icon_cart()

        # Переход к оформлению заказа
        cart_page.clic_to_button_confirm()
        time.sleep(5)

        # Заполнение обязательных полей заказа
        confirm_page.enter_required_data()
        time.sleep(5)

        # Кликаем "оформить заказ"
        confirm_page.clic_to_button_confirm()

        #Проверяем, что статус заказа Принят
        assert order_page.check_order_status(), "Заказ не оформлен"

# НЕГАТИВНЫЕ ТЕСТЫ
@pytest.mark.usefixtures("init_driver", "base_url")
class TestRemoveItem:

    def test_add_product_to_cart(self, base_url):
        # Инициализация страницы
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта, который хотим добавить в корзину
        product_id = '253354771'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)

        # Проверка, что товар добавлен в корзину
        assert start_page.is_product_added_to_cart(), "Product was not added to cart"
        time.sleep(5)

        # Кликаем по корзине справа наверху
        start_page.clic_to_icon_cart()
        time.sleep(5)
        # Кликаем по удалить
        cart_page.clic_to_icon_trash(product_id)
        time.sleep(5)
        #Проверка, что форма заказа не видна при удалении товаров из корзины
        assert cart_page.form_order_locator().is_displayed() == False , "Форма заказа видна"

@pytest.mark.usefixtures("init_driver", "base_url")
class TestInvalidPromo:

    def test_add_product_to_cart(self, base_url):
        # Инициализация страницы
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта, который хотим добавить в корзину
        product_id = '253354942'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)

        # Проверка, что товар добавлен в корзину
        assert start_page.is_product_added_to_cart(), "Product was not added to cart"
        time.sleep(5)
        # Кликаем по корзине справа наверху
        start_page.clic_to_icon_cart()

        #Вводим промокод
        cart_page.input_promo()

        #Кликаем применить промокод
        cart_page.clic_to_button_promo()

        # Проверка, что появилось сообщение "Указан несущ купон"
        assert cart_page.text_promo().count('Указан несуществующий купон, убедитесь, что он введен верно') == 1

@pytest.mark.usefixtures("init_driver", "base_url")
class TestInvalidClient:

    def test_add_product_to_cart(self, base_url):
        # Инициализация страницы
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)
        confirm_page = ConfirmPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта, который хотим добавить в корзину
        product_id = '253354771'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)
        time.sleep(3)
        # Кликаем по корзине справа наверху
        start_page.clic_to_icon_cart()

        # Кликаем по "оформить заказ"
        cart_page.clic_to_button_confirm()
        time.sleep(5)

        #Оставляем все поля пустыми и кликаем "Оформить заказ"
        confirm_page.clic_to_button_confirm()
        time.sleep(3)

        # проверяем, что появляется сообщение "Поле не заполнено"
        assert confirm_page.is_text_error().count("Поле не заполнено") == 1
        time.sleep(2)




