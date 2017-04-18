# Funções nativas

[Lista de funções nativas disponíveis no Python](https://docs.python.org/3.6/library/functions.html)

#### abs(x)
Retorna o valor absoluto de um número

---
#### all(iterable)
Retorna True se todos os elementos do `iterable` forem True:

```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

---
#### any(iterable)
Retorna True se qualquer elemento de `iterable` for True:
```python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

---
#### ascii(objeto)
Retorna uma string contendo a representação de um objeto, assim como o `repr()` mas escapa os caracteres que não são ASCII na string retornada por `repr()`, usando escapes como `\x`, `\u` e `\U`

---
#### bin(x)
Converte um número inteiro para uma string em binário

---
#### class bool([x])
Retorna um valor booleano, ou True ou False. A classe `bool` é uma subclasse de `int`

---
#### class bytearray([source[, encoding[, errors]]])
Retorna um novo array de bytes. A classe `bytearray` é uma sequência mutável de números inteiros que pode variar entre `0 <= x < 256`

---
#### class bytes([source[, encoding[, errors]]])
Retorna um novo objeto `bytes` que é uma sequência imutável de números inteiros que pode variar entre `0 <= x < 256`. `bytes` é uma versão imutável de `bytearray`

---
#### callable(objeto)
Retorna `True` se o objeto argumento aparece callable, e `False` se não.

---
#### chr(i)
Retorna a representaçào em string de um caractere cujo Unicode é o número inteiro `i` passado como parâmetro. Por exemplo, `chr(97)` retorna a string 'a'

---
#### classmethod(função)
Retorna um class method para `função`

Um método de classe recebe de maneira implícita a classe como primeiro argumento, igual um instance method recebe uma instância como primeiro parâmetro.

Sintaxe para definir um classmethod:

```python
class C:
    @classmethod
    def f(cls, arg1, arg2, ...): ...
```

A forma `@classmethod` é uma função decorator.

---
#### compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
Compila o `source` passado como parâmetro para código ou para uma AST (Árvore sintática abstrata)

---
#### class complex([real[, imag]])
Retorna um número complexo

---
#### delattr(objeto, nome)
Os argumentos são um objeto e uma string. A string `nome` precisa ser o nome de um dos atributos do objeto. Essa função deleta esse atributo. `delattr(x, 'foobar')` é equivalente a `del x.foobar`

---
#### class dict(**kwarg)
Cria um novo dicionário.

kwargs significa `keyword arguments`

---
#### dir([objeto])
Sem argumentos, retorna a lista de nomes dentro do escopo local atual. Com argumento tenta retornar uma lista de atributos válidos para o objeto.

```python
>>> import struct
>>> dir()   # show the names in the module namespace
['__builtins__', '__name__', 'struct']
>>> dir(struct)   # show the names in the struct module
['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
 '__initializing__', '__loader__', '__name__', '__package__',
 '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']
```

---
#### divmod(a, b)
Recebe dois números e retorna um par de números que são o quociente e o restante ao se utilizar divisão de números inteiros.

---
#### enumerate(iterable, start = 0)
Retorna um objeto `enumerate`

---
#### eval(expression, globals=None, locals=None)


---
#### exec(objeto[, globals[, locals]])
Essa função suporta execução dinâmica de código Python

---
#### filter(function, iterable)
Constrõe um iterador para os elementos em `iterable` para quais a função retorna True

`filter(function, iterable)` é equivalente a `(item for item in iterable if function(item)) if function is not None and (item for item in iterable if item) if function is None`
--------------------------------------------------------------------------------------------
#### float([x])
`x` pode ser um númeor ou string, Função retorna um número float

---
#### format(value[, format_spec])
Converte um valor para uma versão 'formatada'.

---
#### class frozenset([iterable])
Retorna um objeto `frozenset`

---
#### getattr(bject, name[, default])
Retorna o valor do atributo do objeto, `name` precisa ser uma string

---
#### globals()


---
#### hasattr(objeto, name)
Recebe um objeto e uma string. Retorna True se `name` é um nome de um dos atributos do objeto

---
#### hash(objeto)
Retorna o valor em hash de um objeto. É usado para comparar rapidamente chaves em dicionários.

---
#### help([objeto])
Invoca o sistema de ajuda

---
#### hex(x)
Converte um número inteiro para uma string hexadecimal
```python
hex(255)
'0xff'
```

---
#### id(objeto)
Retorna a 'identidade' de um objeto

---
#### input([prompt])


---
#### int(x=0)
Retorna um objeto de número inteiro a partir de um número inteiro ou uma string `x`

---
#### isinstance(objeto, classinfo)


---
#### issubclass(class, classinfo)


---
#### iter(objeto[, sentinel])


---
#### len(s)
Retorna o length (o número de itens) de um objeto

---
#### class list([iterable])


---
#### locals()


---
#### map(function, iterable, ...)


---
#### max(iterable, *[, key, default])


---
#### memoryview(objeto)


---
#### min(iterable, *[, key, default])


---
#### next(iterator[, default])


---
#### class object


---
#### oct(x)


---
#### open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
Abre um arquivo e retorna um `objeto file` correspondente.

---
#### ord(c)


---
#### pow(x, y[, z])


---
#### print(*objetos, sep=' ', end='\n', file=sys.stdout, flush=False)


---
#### class property(fget=None, fset=None, fdel=None, doc=None)
Retorna uma propriedade atributo

---
#### range(start, stop[, step])
Representa uma sequência de números

```python
# range(start, end, incrementor)

def get_me_range_incrementor():
    for number in range(4, 10, 2):  # 4 6 8
        print(number)

get_me_range_incrementor()
```

---
#### repr(objeto)
Retorna uma string contendo a representação de um objeto

---
#### reversed(seq)
Retorna o iterador de maneira reversa

---
#### round(number[, ndigits])
Retorna número arredondado

---
#### class set([iterable])
Retorna um objeto `set`

---
#### setattr(objeto, name, value)


---
#### slice(start, stop[, step])


---
#### sorted(iterable[, key][, reverse])
Retorna uma lista ordenada

---
#### staticmethod(function)


---
#### str(objeto=b'', encoding='utf-8', errors='strict')


---
#### sum(iterable[, start])


---
#### super([type[, objeto-or-type]])


---
#### tuple([iterable])
Tuple retorna uma sequência imutável

---
#### type(object) ou type(name, bases, dict)
Com um argumeto retorna o tipo do objeto. Com três argumentos retorna um novo objeto `type`

---
#### vars([objeto])
Retorna o atributo \_\_dict\_\_ de um módulo, classe, instância ou qualquer outro objeto com um atributo \_\_dict\_\_

---
#### zip(*iterables)
Cria um iterador que agrega elementos de cada um dos iterables

```python
def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
```

---
#### \_\_import\_\_()
