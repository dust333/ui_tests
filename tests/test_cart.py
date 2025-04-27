import allure
import pytest
from assertpy import assert_that

from entities.pages.cart import CartPage
from entities.pages.main import MainPage


class TestCart:
    @pytest.mark.cart
    @allure.title("Добавление и удаление товара из корзины")
    def test_cart(self, get_page) -> None:
        main_page = get_page(MainPage)
        cart_page = get_page(CartPage)

        with allure.step("Открытие главной страницы"):
            main_page.open()

        with allure.step("Добавление товара в корзину"):
            main_page.items[0].add_to_cart_button.click()
        with allure.step("Проверка отображения товара в popup корзины"):
            with allure.step("Проверка, что добавлен только 1 товар"):
                assert_that(main_page.cart_popup.items).is_length(1)
            with allure.step("Проверка, что добавлен корректный товар"):
                assert_that(main_page.items[0]).is_equal_to(
                    main_page.cart_popup.items[0]
                )
            main_page.cart_popup.items[0].check_visible()
        with allure.step("Открытие страницы корзины"):
            cart_page.open()

        with allure.step("Проверка отображения товара на странице корзины"):
            with allure.step("Проверка, что отображается только 1 товар"):
                assert len(cart_page.items) == 1
            cart_page.items[0].check_visible()

        with allure.step("Удаление товара из корзины"):
            cart_page.items[0].delete_from_cart_button.click()

        with allure.step("Проверка отсутствия товаров в корзине"):
            cart_page.open()
            cart_page.empty_cart_text.check_visible(timeout=1000)
