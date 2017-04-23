# Funções

### Funções privadas ou reservadas

Funções privadas ou reservadas possuem dois underlines de cada lado `__funcao__`. E elas não podem ser chamadas diretamente

```python
class Gato():
    def __init__(self, name): # Função construtora, chamada automaticamente quando um novo objeto é criado
        self.name = name  # a propriedade "name" é única para cada instância criada
```

#### Outros exemplos de funções privadas

`__str__` e `__repr__` são dois métodos que retornam a representação em string de um objeto.

- `__str__` geralmente entrega uma representação mais curta e mais amigável do objeto
- `__repr__` descreve o objeto em mais detalhes. É a representação **oficial** em string do objeto

```python
class Animal():
    def __str__(): # É uma representação legível para humanos do seu objeto, uma versão em string

    def __repr__(): # Deve ser o mais claro possível. Toda classe deve conter esse método.
```

### Parâmetros default em uma função
```python
def key_words_arguments(name='Gabriel', age=30, height=180):
    print(name, age, height)

# Substitua os argumentos que você deseja referenciando eles diretamente
key_words_arguments(age=32, height=160) # A função sabe qual argumento se deseja substituir
```

### Argumentos flexíveis com (\*args), parecidos com parâmetros rest em Javascript
```python
def funcao_variadica(*args):
    print(type(args)) #<class 'tuple'>
    for a in args:
        print(a)

funcao_variadica(1, 2, 3, 4, 5, 6, 7)
```

Passando uma lista de argumentos para uma função com (\*args)
```python
# Função que desdobra uma lista inteira dentro do argumento da função
body_parts = ['ear', 'leg', 'head', 'arm']

def print_body_parts(*args):
    for a in args:
        print(a)

print_body_parts(*body_parts)
```

### Passando um dicionário para a função com (\*\*kwargs)
```python
def printdict(**kwargs): # kwargs significa "keyword arguments"
    print repr(kwargs)

printdict(john=10, jill=12, david=15)
```
