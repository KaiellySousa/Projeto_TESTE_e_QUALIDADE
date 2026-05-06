# Projeto de Automacao de Testes - Swagger Petstore e SauceDemo

Este projeto apresenta a automacao de testes para a API Swagger Petstore e para a interface web da plataforma SauceDemo. O desenvolvimento foi estruturado seguindo boas praticas de organizacao de codigo e integracao continua.

## Estrutura do Projeto

A organizacao das pastas foi pensada para garantir a separacao de preocupacoes e facilitar a manutencao do codigo:
<img width="243" height="497" alt="image" src="https://github.com/user-attachments/assets/e301c750-a610-43db-ba7b-2ba3eddedc2a" />


## Tecnologias Utilizadas

* **Linguagem**: Python
* **Framework de Testes**: Pytest
* **Automacao Web**: Selenium WebDriver
* **Automacao de API**: Requests library
* **CI/CD**: GitHub Actions

## Instrucoes de Instalacao e Execucao

1. **Clone o repositorio**:
```bash
git clone https://github.com/KaiellySousa/Projeto_TESTE_e_QUALIDADE.git
cd PROJETO_AUTOMACAO
```

2. **Instale as dependencias**:
```bash
pip install -r requirements.txt
```

3. **Execute todos os testes**:
```bash
python -m pytest
```

## Metodologia e Padroes Aplicados

### Page Objects (POM)
Na automacao web, foi aplicado o padrao Page Objects dentro do diretorio `web/pages/`. Esta abordagem isola a estrutura das paginas da logica de teste, facilitando a manutencao caso ocorram mudancas no layout do site.

### Integracao Continua (CI)
O projeto conta com uma pipeline configurada via GitHub Actions no arquivo `pipeline.yml`. A cada commit, a pipeline e acionada para configurar o ambiente, instalar dependencias e executar a suite de testes de forma automatizada.

### Configuracao de Ambiente
Para a execucao na pipeline, o Selenium foi configurado em modo **Headless** (sem interface grafica). Isso garante que os testes de interface rodem corretamente em servidores de integracao continua.

## Cobertura de Testes

1. **API Petstore**:
    * Teste de CRUD completo para Pets.
    * Criacao e validacao de pedidos na Store.
    * Gerenciamento e consulta de Usuarios.
    * Validacao de cenario negativo (ID inexistente).

2. **Web SauceDemo**:
    * Fluxo E2E completo: Login, adicao de produto ao carrinho, preenchimento de dados de entrega e finalizacao da compra com validacao da mensagem de sucesso.
