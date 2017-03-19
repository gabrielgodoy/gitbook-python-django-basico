# Começando com o Django

{% include "../../common/python-and-virtualenv.md" %}

---

## Criando o projeto Django

```bash
# Crie um projeto inicial
django-admin startproject [PROJECT_NAME]
```

Não é necessário rodar o django-admin.py para mais nada, somente para criação do projeto. 
Para todo o resto utilize o utilitário **manage.py**

```bash
# Crie um app dentro desse projeto
python manage.py startapp [APP_NAME]
```

Adicione uma referência do app criado em INSTALLED_APPS no arquivo settings.py
```python
INSTALLED_APPS = [
    someApp.apps.SomeAppConfig
]
```

```bash
# Deixe o banco do Django sincado pela primeira vez, e crie as tabelas para os apps que vem nativos no Django (comandos SQL)
python manage.py migrate
```

## Acessando o admin do Django

```bash
# Crie o usuário que vai acessar o admin do Django
python manage.py createsuperuser
```

```bash
# Rode o mini servidor que vem com o Django
python manage.py runserver
```

Agora acesse `http://localhost:8000/admin`

Ao rodar esse comando, o Django também cria o arquivo chamado **db.sqlite3** com o banco de dados padrão


## Arquivos estáticos (imagens, js, css)
Crie uma pasta chamada static e dentro uma pasta com o nome do seu app, e coloque todos os assets estáticos /app/static/app

Entre no arquivo `settings.py` e configure a variável **STATIC_ROOT**

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
