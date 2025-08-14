# Mini To-Do List com Django

Um simples aplicativo de lista de tarefas (To-Do list) desenvolvido com Django.

## Estrutura do Projeto

```
Todo_List_Django/
├── db.sqlite3
├── instrucoes.txt
├── manage.py
├── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       ├── base.html
│       ├── cadastro.html
│       ├── login.html
│       └── tasks/
├── todoproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
└── venv/
```

## Tecnologias Utilizadas

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS, Bootstrap
*   **Banco de Dados:** SQLite (padrão do Django para desenvolvimento)

## Como Baixar o Projeto

1.  Clone o repositório (substitua a URL pelo link do seu repositório):
    ```bash
    https://github.com/renaneliakim1/Todo_List_Django.git
    ```

## Instalação

1.  **Crie e ative um ambiente virtual:**

    *No Windows:*
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    *No macOS/Linux:*
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Instale as dependências:**

    Instale o Django:
    ```bash
    pip install Django
    ```
    *(Recomenda-se criar um arquivo `requirements.txt` com `pip freeze > requirements.txt` para facilitar a instalação em outros ambientes.)*

## Como Executar a Aplicação

1.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

2.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

3.  Abra seu navegador e acesse `http://127.0.0.1:8000/` para ver a aplicação em funcionamento.

## Funcionalidades

*   Cadastro de usuários
*   Login e Logout de usuários
*   Criação, visualização, edição e exclusão de tarefas
*   As tarefas são associadas a cada usuário.
