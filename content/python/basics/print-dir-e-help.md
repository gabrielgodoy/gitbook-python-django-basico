# print()
Serve para imprimir o valor de alguma variável da tela

```python
a = 2
print(a) # 2
```

# dir()

Exibe todo os métodos exstentes em um determinado objeto

```python
dir("teste")

'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 
'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''
```

{% hint style='info' %}
Quando o método começa e termina com dois underlines `__METODO__` significa que estes métodos são privados, que não podem ser chamados diretamente 
{% endhint %}


# help()

Exibe detalhes sobre um determinado método

```python
algumaString = "ok"

help(algumaString.upper)

'''
Help on built-in function upper:

upper(...) method of builtins.str instance
    S.upper() -> str

    Return a copy of S converted to uppercase.
'''
```
