# Funções

[Lista de funções nativas disponíveis no Python](https://docs.python.org/3.6/library/functions.html)

```python
# Default parameters
def key_words_arguments(name='Gabriel', age=30, height=180):
    print(name, age, height)
```

```python
# Substitua os argumentos que você deseja referenciando eles diretamente
# A função sabe qual argumento se deseja substituir
key_words_arguments(age=32, height=160)
```

```python
# Argumentos flexíveis, parecidos com rest params em Javascript
def variadic_function(*args):
    print(type(args)) #<class 'tuple'>
    for a in args:
        print(a)

variadic_function(1, 2, 3, 4, 5, 6, 7)
```

Passando uma lista de argumentos para uma função com \*

```python
# Função que desdobra uma lista inteira dentro do argumento da função
body_parts = ['ear', 'leg', 'head', 'arm']

def print_body_parts(*args):
    for a in args:
        print(a)

print_body_parts(*body_parts)
```


Passando um dicionário para a função com \*\*
```python
def printdict(**kwargs):
    print repr(kwargs)

printdict(john=10, jill=12, david=15)
```


## Exemplo de funções nativas

### range()

```python
# Range method => range(start, end, incrementor)

def get_me_range_incrementor():
    for number in range(4, 10, 2):  # 4 6 8
        print(number)

get_me_range_incrementor()
```

### len()
Return the length (the number of items) of an object.
