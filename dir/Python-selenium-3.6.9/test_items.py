import time


def test_check_basket_button_name(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    basket_button = browser.find_element_by_css_selector("#add_to_basket_form > button").get_attribute('value')
    language = browser.find_element_by_css_selector("#language_selector > div > select").get_attribute('selectedIndex')

    if language == '0':
        assert "أضف الى سلة التسوق" == basket_button
    if language == '1':
        assert "Afegeix a la cistella" == basket_button
    if language == '2':
        assert "Vložit do košíku" == basket_button
    if language == '3':
        assert "Læg i kurv" == basket_button
    if language == '4':
        assert "In Warenkorb legen" == basket_button
    if language == '5':
        assert "Add to basket" == basket_button
    if language == '6':
        assert "Προσθήκη στο καλάθι" == basket_button
    if language == '7':
        assert "Añadir al carrito" == basket_button
    if language == '8':
        assert "Lisää koriin" == basket_button
    if language == '9':
        assert "Ajouter au panier" == basket_button
    if language == '10':
        assert "Aggiungi al carrello" == basket_button
    if language == '11':
        assert "장바구니 담기" == basket_button
    if language == '12':
        assert "Voeg aan winkelmand toe" == basket_button
    if language == '13':
        assert "Dodaj do koszyka" == basket_button
    if language == '14':
        assert "Adicionar ao carrinho" == basket_button
    if language == '15':
        assert "Adicionar à cesta" == basket_button
    if language == '16':
        assert "Adauga in cos" == basket_button
    if language == '17':
        assert "Добавить в корзину" == basket_button
    if language == '18':
        assert "Pridať do košíka" == basket_button
    if language == '19':
        assert "Додати в кошик" == basket_button