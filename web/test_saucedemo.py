import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from .pages.saucedemo_pages import SaucedemoPage

@pytest.fixture
def navegador():
    """Configura o driver do Chrome para os testes."""
    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument("--headless") 
    opcoes.add_argument("--no-sandbox")
    opcoes.add_argument("--disable-dev-shm-usage")
    
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=opcoes)
    driver.implicitly_wait(10)  
    
    yield driver
    driver.quit()

def test_fluxo_compra(navegador):
    """Teste principal: Login, adição ao carrinho e finalização de compra."""
    pagina = SaucedemoPage(navegador)
    
    navegador.get("https://www.saucedemo.com/")
    
    pagina.fazer_login("standard_user", "secret_sauce")
    
    pagina.adicionar_ao_carrinho_e_iniciar_checkout()
    
    pagina.preencher_informacoes_e_finalizar("Kaielly", "Sousa", "64000-000")
    
    # 5. Validação do sucesso da compra
    texto_confirmacao = navegador.find_element(By.CLASS_NAME, "complete-header").text
    assert "obrigada" in texto_confirmacao