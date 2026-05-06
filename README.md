# QA Automation — Petstore API & SauceDemo E2E

Projeto de automação de testes desenvolvido como prova pratica, com testes de API REST e testes E2E web com pipeline de CI integrada.

---

## Tecnologias Utilizadas

### Automação de API
- **Python 3.12+**
- **Pytest** — framework de testes
- **Requests** — cliente HTTP para chamadas à API
- **Petstore Swagger API** — `https://petstore.swagger.io/v2`

### Automação Web (E2E)
- **Python 3.12+**
- **Pytest** — framework de testes
- **Selenium WebDriver 4.21+** — automação do navegador
- **SauceDemo (Swag Labs)** — `https://www.saucedemo.com`

### CI/CD
- **GitHub Actions** — pipelines automáticas a cada push ou pull request

---

## Como Executar Localmente

### Pré-requisitos
- Python 3.12+
- Google Chrome instalado
- Git

### 1. Testes de API — Petstore

```bash
cd Teste_API
pip install -r requirements.txt
python -m pytest -v
```

### 2. Testes E2E — SauceDemo

```bash
cd Teste_E2E
pip install -r requirements.txt
python -m pytest -v
```

> O Selenium Manager (incluso no Selenium 4.6+).

---

## Cenários de Teste

### API — Petstore (`18 testes`)

| Módulo | Cenário |
|--------|---------|
| Pet | Criar, buscar, atualizar, buscar por status, deletar, verificar 404 após deleção |
| Store | Consultar inventário, criar pedido, buscar pedido, deletar pedido, verificar 404 |
| User | Criar, buscar, atualizar, login, logout, deletar, verificar 404 |

### E2E — SauceDemo (`4 testes`)

| Cenário | Descrição |
|---------|-----------|
| Login válido | Realiza login com credenciais corretas e valida redirecionamento |
| Login inválido | Tenta login com credenciais erradas e valida mensagem de erro |
| Adicionar produtos | Adiciona todos os produtos ao carrinho e valida o contador |
| Fluxo completo | Login → adicionar produtos → carrinho → checkout → confirmação |

---

## Design Pattern — Page Objects

A automação web utiliza o padrão **Page Object Model (POM)**, onde cada página do sistema é representada por uma classe responsável pelos seus elementos e ações. Isso garante reusabilidade e facilidade de manutenção.

```
LoginPage       → login()
InventoryPage   → add_all_products(), go_to_cart()
CartPage        → proceed_to_checkout()
CheckoutPage    → fill_personal_info(), finish_purchase()
ConfirmationPage → is_order_confirmed()
```

---

## CI/CD — GitHub Actions

As pipelines são disparadas automaticamente a cada `push` ou `pull request`, cada uma monitorando sua respectiva pasta:

- `api-tests.yml` → roda quando há mudanças em `Teste_API/`
- `web-tests.yml` → roda quando há mudanças em `Teste_E2E/`

---

## Prints de Execução

### API — 18/18 testes passando
<img width="549" height="282" alt="image" src="https://github.com/user-attachments/assets/8f8bf266-fdc8-4b10-af27-a269e05e8311" />


### E2E — 4/4 testes passando
<img width="943" height="408" alt="image" src="https://github.com/user-attachments/assets/3235bb36-3f4d-4803-b78e-5b02da49f811" />

### WEb —
<img width="1918" height="986" alt="image" src="https://github.com/user-attachments/assets/6932ad76-0d5d-440d-b7cd-a170f582e528" />
<img width="1909" height="793" alt="image" src="https://github.com/user-attachments/assets/0a44b981-1c90-4e6c-a3ac-69ab58bfc48c" />

### Pipeline —
<img width="1510" height="476" alt="image" src="https://github.com/user-attachments/assets/c91b9511-3dc8-4edc-92aa-56bc699e6a86" />

