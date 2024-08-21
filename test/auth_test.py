import allure
from page.AuthPage import AuthPage
from page.MainPage import MainPage

def test_auth(browser):
    email = "din.tan1995@mail.ru"
    password = "mAd251@10TaPi"
    username = "Диана"

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()

    info = main_page.get_account_info()

    current_url = main_page.get_current_url()
    
    with allure.step("Проверить, что URL " + current_url + "заканчивается на user86585037/boards"):
        assert current_url.endswith("user86585037/boards")
    
    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть " + username):
            assert info[0] == username
        with allure.step("Почта пользователя должна быть " + email):
            assert info[1] == email