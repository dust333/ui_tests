from dataclasses import dataclass


@dataclass
class User:
    email: str
    password: str
    first_name: str
    second_name: str


class TestUsers:
    admin = ...  # пример наполнения
    basic = User(
        email="forez1757@gmail.com",
        password="P@ssw0rd",
        first_name="Иван",
        second_name="Иванов",
    )
