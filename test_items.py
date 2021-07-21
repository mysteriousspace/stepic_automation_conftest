import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_items(browser):
    browser.get(link)
    time.sleep(10)
    result = browser.find_element_by_class_name('btn.btn-lg.btn-primary').text
    assert result == 'Añadir al carrito', 'message is not "Añadir al carrito!"'
