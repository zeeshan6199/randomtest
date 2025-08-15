from playwright.sync_api import Page,expect
from pages.productspage import ProductPage

def test_confirmation(logged_in):
    prodpage=ProductPage(logged_in)
    expect(prodpage.verifyonpage()).to_be_hidden()


