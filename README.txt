LEDGERFLOW - NOVA CONTA

**LedgerFlow** é uma aplicação web desenvolvida para a **NOVA CONTA**, com o objetivo de centralizar o **cadastro de clientes**, o **controle de boletos/mensalidades** e o **acompanhamento financeiro** da empresa.

A solução foi criada para substituir controles manuais em planilhas, reduzindo falhas operacionais, melhorando a organização administrativa e oferecendo uma interface moderna, acessível e eficiente, alinhada à identidade visual da **NOVA CONTA**, baseada nas cores **branco, vermelho e preto**.

O sistema foi estruturado para atender aos requisitos do **Projeto Integrador**, contemplando framework web, banco de dados, interface com HTML/CSS/JavaScript, acessibilidade, versionamento, API e possibilidade de expansão para deploy em nuvem.

---

# Funcionalidades

### Tela Inicial

Página de apresentação do sistema, explicando a finalidade do LedgerFlow e permitindo acesso ao login.

### Autenticação de Usuários

Controle de acesso para colaboradores cadastrados no sistema.

### Dashboard Administrativo

Painel com visão geral contendo:

* total de clientes cadastrados
* total de boletos registrados
* boletos pagos
* boletos pendentes
* boletos atrasados

Também inclui gráfico de resumo financeiro.

### Cadastro de Clientes

Permite registrar novos clientes com:

* nome
* empresa
* cidade
* e-mail
* telefone
* CPF/CNPJ

### Listagem de Clientes

Tabela completa com todos os clientes cadastrados.

### Cadastro de Boletos

Permite registrar novas mensalidades vinculadas aos clientes contendo:

* cliente
* descrição
* valor
* vencimento
* status
* código do boleto

### Listagem de Boletos

Visualização de todas as mensalidades cadastradas no sistema.

### API REST

Endpoint disponível para consulta de clientes em formato JSON.

### Banco de Dados Populado

O sistema gera automaticamente:

* **200 clientes fictícios**
* **7 colaboradores fictícios**
* várias mensalidades associadas aos clientes

### Interface Responsiva

Layout adaptado para diferentes tamanhos de tela.

---

# Tecnologias Utilizadas

Backend

* Python
* Flask

Banco de Dados

* SQLite

Frontend

* HTML
* CSS
* JavaScript

Bibliotecas

* Flask-Login
* Flask-SQLAlchemy
* Faker
* Chart.js

Controle de Versão

* Git
* GitHub

Possibilidade de Deploy Futuro

* Render
* Railway
* PythonAnywhere

---

# Pré-requisitos

Para executar o projeto é necessário possuir instalado:

* Python 3.x
* Git
* VS Code ou outro editor compatível

---

# Instalação

## 1. Abra a pasta do projeto

Abra a pasta do projeto no **VS Code**.

---

## 2. Crie o ambiente virtual

No terminal execute:

```bash
python -m venv .venv
```

---

## 3. Ative o ambiente virtual

No PowerShell:

```bash
.venv\Scripts\activate
```

Se o Windows bloquear a execução de scripts:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois execute novamente:

```bash
.venv\Scripts\activate
```

---

## 4. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

---

## 5. Gere o banco de dados

```bash
python seed.py
```

Este comando cria automaticamente:

* 7 colaboradores fictícios
* 200 clientes fictícios
* várias mensalidades

---

## 6. Execute o sistema

```bash
python run.py
```

Abra no navegador:

```
http://127.0.0.1:5000/
```

---

# Login de Teste

Use o seguinte usuário para acessar o sistema:

Email

```
user0@novaconta.com.br
```

Senha

```
123456
```

Também existem outros usuários de teste:

```
user1@novaconta.com.br
user2@novaconta.com.br
user3@novaconta.com.br
```

Todos com senha:

```
123456
```

---

# Rotas Principais

Tela inicial

```
http://127.0.0.1:5000/
```

Login

```
http://127.0.0.1:5000/login
```

Dashboard

```
http://127.0.0.1:5000/dashboard
```

Clientes

```
http://127.0.0.1:5000/clientes/
```

Cadastrar cliente

```
http://127.0.0.1:5000/clientes/novo
```

Boletos / Mensalidades

```
http://127.0.0.1:5000/financeiro/mensalidades
```

Cadastrar boleto

```
http://127.0.0.1:5000/financeiro/boletos/novo
```

API de clientes

```
http://127.0.0.1:5000/api/clientes
```

---

# Estrutura do Projeto

```
Ledgerflow/
│
├── run.py
├── config.py
├── requirements.txt
├── seed.py
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   │
│   ├── routes/
│   │   ├── main.py
│   │   ├── auth.py
│   │   ├── clientes.py
│   │   ├── financeiro.py
│   │   └── api.py
│   │
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── clientes.html
│   │   ├── cadastrar_cliente.html
│   │   ├── mensalidades.html
│   │   └── cadastrar_boleto.html
│   │
│   └── static/
│       └── style.css
│
└── instance/
    └── ledgerflow.db
```

---

# Banco de Dados

O sistema utiliza **SQLite**, adequado para aplicações locais e projetos acadêmicos.

### Tabelas principais

**colaboradores**

* id
* nome
* email
* senha
* cargo

**clientes**

* id
* nome
* empresa
* cidade
* email
* telefone
* documento

**mensalidades**

* id
* cliente_id
* descricao
* valor
* vencimento
* status
* codigo_boleto

---

# API

O sistema disponibiliza um endpoint para consulta de clientes:

```
GET /api/clientes
```

Exemplo de retorno:

```json
[
  {
    "id": 1,
    "nome": "João da Silva",
    "empresa": "Silva Contábil",
    "cidade": "São Paulo",
    "email": "joao@email.com",
    "telefone": "(11) 99999-0000"
  }
]
```

Essa estrutura permite futuras integrações com outros sistemas.

---

# Dados Fictícios

Todos os dados presentes no sistema são **fictícios** e foram gerados automaticamente pela biblioteca **Faker**, sendo utilizados apenas para:

* testes
* demonstração
* validação do sistema

---

# Próximas Evoluções

Possíveis melhorias futuras:

* edição de clientes
* exclusão de clientes
* baixa automática de boletos
* relatórios financeiros em PDF
* exportação para Excel
* criptografia de senha
* dashboards analíticos
* deploy em nuvem
* integração com APIs bancárias

---

# Licença

Este projeto foi desenvolvido para **fins acadêmicos**, no contexto de um **Projeto Integrador**, e não possui licença pública definida.

---

# Autoria

Projeto desenvolvido para o **Projeto Integrador da UNIVESP**, com foco em sistemas web aplicados à gestão administrativa.

**Sistema:** LedgerFlow
**Aplicação:** gestão de clientes e controle de mensalidades
**Tecnologia principal:** Python + Flask

