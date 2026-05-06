# web/test_saucedemo.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from web.pages.saucedemo_pages import SaucedemoPage

@pytest.fixture
def navegador():
    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument("--headless")
    opcoes.add_argument("--no-sandbox")
    opcoes.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=opcoes)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_fluxo_compra(navegador):
    pagina = SaucedemoPage(navegador)
    navegador.get("https://www.saucedemo.com/")

    pagina.fazer_login("standard_user", "secret_sauce")
    pagina.adicionar_ao_carrinho_e_iniciar_checkout()
    pagina.preencher_informacoes_e_finalizar("Kaielly", "Sousa", "64000-000")

    texto_confirmacao = navegador.find_element(By.CLASS_NAME, "complete-header").text
    # Asserção exata conforme o site
    assert "Thank you for your order!" in texto_confirmacao