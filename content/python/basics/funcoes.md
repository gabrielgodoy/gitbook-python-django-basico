# Funções

```python
# Default parameters
def param_or_not(param=2):
    print(param)

param_or_not()  # 2
param_or_not(10)  # 10
```

```python
# Keywords with arguments
def key_words_arguments(name='Gabriel', age=30, height=180):
    print(name, age, height)
```

```python
# Substitua os argumentos que você deseja referenciando eles diretamente.
# A função sabe qual argumento se deseja substituir
key_words_arguments(age=32, height=160)
```

```python
# Argumentos flexíveis, parecidos com rest params em Javascript
def variadic_function(*args):
    print(type(args))
    for a in args:
        print(a)

variadic_function(1, 2, 3, 4, 5, 6, 7)
```

```python
# Função que desdobra uma lista inteira dentro do argumento da função
body_parts = ['ear', 'leg', 'head', 'arm']

def print_body_parts(*args):
    for a in args:
        print(a)

print_body_parts(*body_parts)
```
