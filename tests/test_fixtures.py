import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("Данная фикстура будет запущена автоматически перед каждым автотестом")

@pytest.fixture(scope="function")
def browser():
    print("Данная фикстура будет запущена на каждый автотест")

@pytest.fixture(scope="class")
def user():
    print("Данная фикстура будет запущена на каждый тестовый класс")

@pytest.fixture(scope="session")
def settings():
    print("Данная фикстура будет запущена один раз на всю тестовую сессию")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...