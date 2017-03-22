# MVC aplicado ao Django

O Django possui uma arquitetura separada em Model, View e Controller (MVC). 

A arquitetura MVC separa as responsabilidades da aplicação e torna o código mais legível.

{% hint style='info' %}
Na verdade o Django é muitas vezes visto como uma arquitetura **MTV (Model, Template e View)**
{% endhint %}

## Model

No model é definido o "molde", ou estrutura dos dados da sua aplicação. No Django esse molde dos dados é feito no arquivo `models-py` do seu app, através de classes que descrevem a estrutura de um determinado dado.

Exemplo de uma classe no `models.py` no Django:

```python
class Pessoa(models.Model):
     nome = models.CharField(max_length=50)
     idade = models.IntegerField()
```

## View

A view é a camada de apresentação do seu site ao usuário final. Na view são exibidos os dados do model ao usuário. **Esse papel é feito pelos templates no caso do Django**.


## Controller

O controller é responsável por ligar os model com as views e realizar qualquer lógica intermediária entre eles como manipulação de dados. O controller, como o nome já diz, controla a maneira como os dados fluem entre o model e a view, e vice-versa.

O controller no Django fica em grande parte por baixo dos panos do próprio framework.

O papel do controller no Django pode ser atribuído a suas views também, que escolhem qual conteúdo serão exibidos em cada template.
