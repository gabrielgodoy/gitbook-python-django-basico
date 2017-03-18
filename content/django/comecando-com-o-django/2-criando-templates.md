# Crie templates para seus apps

Crie uma pasta chamada **templates** dentro da pasta do seu app
Dentro dessa pasta templates, crie uma pasta com o nome do seu app

Dentro de **views.py** do seu app, importe o render do Django

```python
from django.shortcuts import render
```

Dentro de cada função view, retorne o método render com o seu template, context significa o conteúdo do banco de dados que você deseja injetar dentro do seu template.

```python
return render(request, 'Caminho para o arquivo HTML, context)
```

{% raw %}
## Diferença entre **{% %}** e **{{ }}** no Django templates

**{%   %}**   Essa tag pode exibir conteúdo, servir como estrutura de controle, como 'if', 'else' e 'for', ou para resgatar conteúdo vindo do banco de dados

**{{  }}**   Essa tag pode exibir conteúdo que foi definido no context da view, que é um objeto como o dict, com keys e values

## Templates base
Coloque os templates base na mesma pasta dos outros templates, e extenda eles para as outras páginas. As outras páginas podem sobrescrever block pré-definidos dentro do template principal do arquivo HTML. As outras páginas vão 'preencher' o {% block content %} do template.

{% endraw %}
