# Criando os Models

Models que dão a forma ao seus dados dentro do banco de dados

No arquivo `models.py`, crie a classe para o seu model com os campos que você deseja

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

## Registre novos Models no admin do App

Vá para a pasta do app e edite o arquivo admin.py

Importe a classe do model

```python
from .models import [Some_model]
```

Registre seu model no admin.py

```python
admin.site.register(Some_model)
```

### Mude como os seus models são exibidos dentro do admin do Django

```python
def __str__(self):
    return self.name
```
