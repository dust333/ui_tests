import allure
import pytest
from assertpy import assert_that

from entities.pages.favorites import FavoritePage
from entities.pages.main import MainPage


class TestFavorites:
    @pytest.mark.favorites
    @allure.title("Добавление товара в избранное")
    def test_favorites(self, get_page) -> None:
        main_page = get_page(MainPage)
        favorite_page = get_page(FavoritePage)

        with allure.step("Открытие главной страницы"):
            main_page.open()

        with allure.step("Добавление товара в избранное"):
            main_page.items[0].add_to_favorite_button.click()
        with allure.step("Открытие страницы Избранное"):
            favorite_page.open()

        with allure.step("Проверка отображения товара"):
            with allure.step("Проверка, что добавлен только 1 товар"):
                assert_that(favorite_page.items).is_length(1)
            with allure.step("Проверка, что добавлен корректный товар"):
                assert_that(main_page.items[0]).is_equal_to(favorite_page.items[0])
        with allure.step("Проверка отображения добавленного товара"):
            favorite_page.items[0].check_visible()
