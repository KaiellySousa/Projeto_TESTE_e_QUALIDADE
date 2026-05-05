from selenium.webdriver.common.by import By

class SaucedemoPage:
    def __init__(self, driver):
        self.driver = driver

    def fazer_login(self, usuario, senha):
        """Realiza o login no sistema SauceDemo."""
        self.driver.find_element(By.ID, "user-name").send_keys(usuario)
        self.driver.find_element(By.ID, "password").send_keys(senha)
        self.driver.find_element(By.ID, "login-button").click()

    def adicionar_ao_carrinho_e_iniciar_checkout(self):
        """Adiciona um produto ao carrinho e inicia o processo de checkout."""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()

    def preencher_informacoes_e_finalizar(self, nome, sobrenome, cep):
        """Preenche os dados de entrega e confirma a compra."""
        self.driver.find_element(By.ID, "first-name").send_keys(nome)
        self.driver.find_element(By.ID, "last-name").send_keys(sobrenome)
        self.driver.find_element(By.ID, "postal-code").send_keys(cep)
        
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.ID, "finish").click()