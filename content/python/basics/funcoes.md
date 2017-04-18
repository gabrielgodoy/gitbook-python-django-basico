# Funções

Parâmetros default
```python
def key_words_arguments(name='Gabriel', age=30, height=180):
    print(name, age, height)

# Substitua os argumentos que você deseja referenciando eles diretamente
# A função sabe qual argumento se deseja substituir
key_words_arguments(age=32, height=160)
```


Argumentos flexíveis, parecidos com parâmetros rest em Javascript
```python
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