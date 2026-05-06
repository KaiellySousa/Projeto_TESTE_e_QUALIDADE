# Projeto de Automacao de Testes - Swagger Petstore e SauceDemo

Este projeto apresenta a automacao de testes para a API Swagger Petstore e para a interface web da plataforma SauceDemo. O desenvolvimento foi estruturado seguindo boas praticas de organizacao de codigo e integracao continua.

## Estrutura do Projeto

A organizacao das pastas foi pensada para garantir a separacao de preocupacoes e facilitar a manutencao do codigo:
''
PROJETO_AUTOMACAO/
├── .github/workflows/    # Configuracao da Pipeline de CI
│   └── pipeline.yml      # Execucao automatica dos testes no GitHub
├── api/                  # Testes de API
│   └── test_petstore.py  # Cobertura de endpoints (User, Store e Pet)
├── web/                  # Testes de Interface Web
│   ├── pages/            # Implementacao do padrao Page Objects
│   │   └── saucedemo_pages.py
│   └── test_saucedemo.py # Fluxo funcional ponta a ponta (E2E)
├── .gitignore            # Arquivos ignorados pelo controle de versao
└── requirements.txt      # Dependencias do projeto (Selenium, Pytest, Requests)
''

## Tecnologias Utilizadas

* Linguagem: Python
* Framework de Testes: Pytest
* Automacao Web: Selenium WebDriver
* Automacao de API: Requests library
* CI/CD: GitHub Actions

## Instrucoes de Instalacao e Execucao

1. Clone o repositorio:
''git clone [https://github.com/KaiellySousa/Projeto_TESTE_e_QUALIDADE.git]
cd PROJETO_AUTOMACAO''

2. Instale as dependencias:
''pip install -r requirements.txt''

3. Execute todos os testes:
''python -m pytest''

## Metodologia e Padroes Aplicados

### Page Objects (POM)
Na automacao web, foi aplicado o padrao Page Objects dentro do diretorio web/pages/. Esta abordagem isola a estrutura das paginas da logica de teste, permitindo que alteracoes no layout do site exijam mudancas apenas na classe da pagina, sem afetar os scripts de teste principais.

### Integracao Continua (CI)
O projeto conta com uma pipeline configurada via GitHub Actions no arquivo pipeline.yml. A cada commit realizado no repositorio, a pipeline e acionada para configurar o ambiente Python, instalar as dependencias e executar a suite de testes completa de forma automatizada.

### Configuracao de Ambiente
Para a execucao na pipeline, o Selenium foi configurado em modo Headless (sem interface grafica) utilizando os argumentos --no-sandbox e --disable-dev-shm-usage. Isso garante que os testes de interface rodem corretamente em servidores de integracao continua.

## Cobertura de Testes

1. API Petstore:
* Teste de CRUD completo para Pets.
* Criacao e validacao de pedidos na Store.
* Gerenciamento e consulta de Usuarios.
* Validacao de cenario negativo (ID inexistente).

2. Web SauceDemo:
* Fluxo E2E completo: Login, adicao de produto ao carrinho, preenchimento de dados de entrega e finalizacao da compra com validacao da mensagem de sucesso.
