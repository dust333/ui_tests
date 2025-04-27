import allure
import pytest
from assertpy import assert_that

from entities.pages.catalog import CatalogPage
from entities.pages.main import MainPage


class TestCatalog:
    @pytest.mark.catalog
    @allure.title("Навигация по каталогу и отображение товаров")
    def test_catalog(self, get_page) -> None:
        main_page = get_page(MainPage)
        catalog_page = get_page(CatalogPage)

        with allure.step("Открытие главной страницы"):
            main_page.open()

        with allure.step("Открытие каталога из мейн-бара"):
            main_page.head.main_bar.catalog_button.click()  # переработать нейминг и структуру компонентов
        with allure.step("Наведение на категорию Электроника"):
            main_page.head.main_bar.catalog_dropdown.category_link(
                "Электроника"
            ).hover()
        with allure.step("Наведение на субкатегорию Планшеты"):
            main_page.head.main_bar.catalog_dropdown.subcategory_link(
                "Планшеты"
            ).hover()
        with allure.step("Выбор бренда Digma"):
            main_page.head.main_bar.catalog_dropdown.subcategory_brand_link(
                "Digma"
            ).click()

        with allure.step("Проверка наличия и видимости товаров"):
            assert_that(len(catalog_page.items)).is_greater_than(0)
            catalog_page.check_items_visible()
