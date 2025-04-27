import allure
import pytest

from entities.pages.main import MainPage


class TestLogin:
    @pytest.mark.login
    @allure.title("Аутентификация")
    def test_login(self, get_page, users) -> None:
        user = users.basic
        main_page = get_page(MainPage)
        with allure.step("Открытие главной страницы"):
            main_page.open()

        with allure.step("Открытие формы аутентификации"):
            main_page.head.top_bar.personal_account_link.click()
            main_page.head.top_bar.auth_dropdown_component.login_button.click()
        with allure.step("Ввод пользовательских данных"):
            main_page.login_form.login_input.fill(user.email)
            main_page.login_form.password_input.fill(user.password)
        with allure.step("Аутентификация"):
            main_page.login_form.login_button.click()

        with allure.step("Проверка появления учетных данных в топ-баре"):
            main_page.head.top_bar.personal_account_link.check_have_text(
                f"{user.first_name} {user.second_name}",
                timeout=1000,
            )
