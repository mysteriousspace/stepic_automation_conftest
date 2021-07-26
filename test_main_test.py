from Block_Conftest.stepic_automation_conftest.pages.main_page import MainPage
from Block_Conftest.stepic_automation_conftest.pages.login_page import LoginPage

link1 = "http://selenium1py.pythonanywhere.com/"
link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
link3 = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_guest_can_go_to_login_page(browser):
    link = link2
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = link2
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_should_see_form_login_and_register(browser):
    link = link3
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()
