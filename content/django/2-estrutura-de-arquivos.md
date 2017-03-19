# Estrutura de arquivos em Projetos e Apps

## Projeto 

```
📁 projeto
     - __init__.py   Sinaliza ao Python que este diretório é um pacote do Python
     - settings.py   Configurações gerais do site
     - urls.py       Controla as rotas e o que acontece quando o usuário acessa alguma url
     - wsgi.py       Configurações do Webserver gateway interface

- manage.py Ferramenta administrativa com muitas funções, como rodar o servidor do Django
```

### Mais sobre urls.py
 
A configuração do arquivo urls.py é responsável por mapear as URL do seu site

Quando uma URL acessada pelo usuário corresponde com algum padrão configurado nesse arquivo, alguma coisa que foi configurada para aquele padrão acontece 
 
Cada app no Django terá um arquivo próprio url.py dentro da sua pasta para administrar URLs. A configuração das URLs estará contida dentro da pasta de cada App.


# App

```
📁 migrations  Possui arquivos que lidam com a migração dos dados para o banco
     - __init__.py   Sinaliza ao Python que este diretório é um pacote do Python

- __init__.py  Sinaliza ao Python que este diretório é um pacote do Python
- admin.py     Registro de models. Acesso ao banco de dados, deletar usuários, posts, etc...
- apps.py      Arquivo de configuração. Configuração para esse App em específico
- models.py    Estrutura das tabelas para o seu banco de dados
- tests.py     Testes para se certificar que não existem bugs
- views.py     Possui funções que recebem um request do usuário, e respondem com uma página por exemplo.
```
