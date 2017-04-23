# Funções nativas

[Lista de funções nativas disponíveis no Python](https://docs.python.org/3.6/library/functions.html)

||||||
|--------------|
| [abs()](#abs)                  |	[dict()](#class-dict)     |	[help()](#help)       |	[min()](#min)	     | [setattr()](#setattr)      |
| [all()](#all)                  |	[dir()](#dir)      |	[hex()](#hex)        |	[next()](#next)	   | [slice()](#slice)        |
| [any()](#any)                  |	[divmod()](#divmod)   |	[id()](#id)         |	[object()](#class-object)   | [sorted()](#sorted)       |
| [ascii()](#ascii)              |	[enumerate()](#enumerate)|	[input()](#input)      |	[oct()](#oct)	     | [staticmethod()](#staticmethod) |
| [bin()](#bin)                  |	[eval()](#eval)     |	[int()](#int)        |	[open()](#open)	   | [str()](#str)          |
| [bool()](#class-bool)                |	[exec()](#exec)     |	[isinstance()](#isinstance) |	[ord()](#ord)	     | [sum()](#sum)         |
| [bytearray()](#class-bytearray) |	[filter()](#filter)     |	[issubclass()](#issubclass) |	[pow()](#pow)	     | [super()](#super)     |
| [bytes()](#class-bytes)          |	[float()](#float)             |	[iter()](#iter)       |	[print()](#print)	   | [tuple()](#tuple) |
| [callable()](#callable)        |	[format()](#format)             |	[len()](#len)        |	[property()](#class-property) | [type()](#type)   |
| [chr()](#chr)                  |	[frozenset()](#class-frozenset)| [list()](#class-list) |	[range()](#range)	   | [vars()](#vars)     |
| [classmethod()](#classmethod) |	[getattr()](#getattr)  |	[locals()](#locals)     |	[repr()](#repr)	   | [zip()](#zip)          |
| [compile()](#compile)          |	[globals()](#globals)  |	[map()](#map)        |	[reversed()](#reversed) | [__import__()](#import)   |
| [complex()](#class-complex)          |	[hasattr()](#hasattr)  |	[max()](#max)        |	[round()](#round)	   |
| [delattr()](#delattr)          |	[hash()](#hash)     |	[memoryview()](#memoryview) |	[set()](#class-set)	     |

#### abs

`abs(x)`
Retorna o valor absoluto de um número

---
#### all

`all(iterable)`
Retorna True se todos os elementos do `iterable` forem True:

```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

---
#### any

`any(iterable)`
Retorna True se qualquer elemento de `iterable` for True:
```python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

---
#### ascii

`ascii(objeto)`
Retorna uma string contendo a representação de um objeto, assim como o `repr()` mas escapa os caracteres que não são ASCII na string retornada por `repr()`, usando escapes como `\x`, `\u` e `\U`

---
#### bin

`bin(x)`
Converte um número inteiro para uma string em binário

---
#### class bool

`class bool([x])`
Retorna um valor booleano, ou True ou False. A classe `bool` é uma subclasse de `int`

---
#### class bytearray

`class bytearray([source[, encoding[, errors]]])`
Retorna um novo array de bytes. A classe `bytearray` é uma sequência mutável de números inteiros que pode variar entre `0 <= x < 256`

---
#### class bytes

`class bytes([source[, encoding[, errors]]])`
Retorna um novo objeto `bytes` que é uma sequência imutável de números inteiros que pode variar entre `0 <= x < 256`. `bytes` é uma versão imutável de `bytearray`

---
#### callable

`callable(objeto)`
Retorna `True` se o objeto argumento aparece callable, e `False` se não.

---
#### chr

`chr(i)`
Retorna a representaçào em string de um caractere cujo Unicode é o número inteiro `i` passado como parâmetro. Por exemplo, `chr(97)` retorna a string 'a'

---
#### classmethod

`classmethod(função)`
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
#### compile

`compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)`
Compila o `source` passado como parâmetro para código ou para uma AST (Árvore sintática abstrata)

---
#### class complex

`class complex([real[, imag]])`
Retorna um número complexo

---
#### delattr

`delattr(objeto, nome)`
Os argumentos são um objeto e uma string. A string `nome` precisa ser o nome de um dos atributos do objeto. Essa função deleta esse atributo. `delattr(x, 'foobar')` é equivalente a `del x.foobar`

---
#### class dict

`class dict(**kwarg)`
Cria um novo dicionário.

kwargs significa `keyword arguments`

---
#### dir

`dir([objeto])`
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
#### divmod

`divmod(a, b)`
Recebe dois números e retorna um par de números que são o quociente e o restante ao se utilizar divisão de números inteiros.

---
#### enumerate

`enumerate(iterable, start = 0)`
Retorna um objeto `enumerate`

---
#### eval

`eval(expression, globals=None, locals=None)`


---
#### exec

`exec(objeto[, globals[, locals]])`
Essa função suporta execução dinâmica de código Python

---
#### filter

`filter(function, iterable)`
Constrõe um iterador para os elementos em `iterable` para quais a função retorna True

`filter(function, iterable)` é equivalente a `(item for item in iterable if function(item)) if function is not None and (item for item in iterable if item) if function is None`

--------------------------------------------------------------------------------------------

#### float

`float([x])`
`x` pode ser um númeor ou string, Função retorna um número float

---
#### format

`format(value[, format_spec])`
Converte um valor para uma versão 'formatada'.

---
#### class frozenset

`class frozenset([iterable])`
Retorna um objeto `frozenset`

---
#### getattr

`getattr(bject, name[, default])`
Retorna o valor do atributo do objeto, `name` precisa ser uma string

---
#### globals

`globals()`


---
#### hasattr

`hasattr(objeto, name)`
Recebe um objeto e uma string. Retorna True se `name` é um nome de um dos atributos do objeto

---
#### hash

`hash(objeto)`
Retorna o valor em hash de um objeto. É usado para comparar rapidamente chaves em dicionários.

---
#### help

`help([objeto])`
Invoca o sistema de ajuda

---
#### hex

`hex(x)`
Converte um número inteiro para uma string hexadecimal
```python
hex(255)
'0xff'
```

---
#### id

`id(objeto)`
Retorna a 'identidade' de um objeto

---
#### input

`input([prompt])`


---
#### int

`int(x=0)`
Retorna um objeto de número inteiro a partir de um número inteiro ou uma string `x`

---
#### isinstance

`isinstance(objeto, classinfo)`


---
#### issubclass

`issubclass(class, classinfo)`


---
#### iter

`iter(objeto[, sentinel])`


---
#### len

`len(s)`
Retorna o length (o número de itens) de um objeto

---
#### class list

`class list([iterable])`


---
#### locals

`locals()`


---
#### map

`map(function, iterable, ...)`


---
#### max

`max(iterable, *[, key, default])`


---
#### memoryview

`memoryview(objeto)`


---
#### min

`min(iterable, *[, key, default])`


---
#### next

`next(iterator[, default])`


---
#### class object

`class object`


---
#### oct

`oct(x)`


---
#### open

`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`
Abre um arquivo e retorna um `objeto file` correspondente.

---
#### ord

`ord(c)`


---
#### pow

`pow(x, y[, z])`


---
#### print

`print(*objetos, sep=' ', end='\n', file=sys.stdout, flush=False)`


---
#### class property

`class property(fget=None, fset=None, fdel=None, doc=None)`
Retorna uma propriedade atributo

---
#### range

`range(start, stop[, step])`
Representa uma sequência de números

```python
# range(start, end, incrementor)

def get_me_range_incrementor():
    for number in range(4, 10, 2):  # 4 6 8
        print(number)

get_me_range_incrementor()
```

---
#### repr

`repr(objeto)`
Retorna uma string contendo a representação de um objeto

---
#### reversed

`reversed(seq)`
Retorna o iterador de maneira reversa

---
#### round

`round(number[, ndigits])`
Retorna número arredondado

---
#### class set

`class set([iterable])`
Retorna um objeto `set`

---
#### setattr

`setattr(objeto, name, value)`


---
#### slice

`slice(start, stop[, step])`


---
#### sorted

`sorted(iterable[, key][, reverse])`
Retorna uma lista ordenada

---
#### staticmethod

`staticmethod(function)`


---
#### str

`str(objeto=b'', encoding='utf-8', errors='strict')`


---
#### sum

`sum(iterable[, start])`


---
#### super

`super([type[, objeto-or-type]])`


---
#### tuple

`tuple([iterable])`
Tuple retorna uma sequência imutável

---
#### type

`type(object) ou type(name, bases, dict)`
Com um argumeto retorna o tipo do objeto. Com três argumentos retorna um novo objeto `type`

---
#### vars

`vars([objeto])`
Retorna o atributo \_\_dict\_\_ de um módulo, classe, instância ou qualquer outro objeto com um atributo \_\_dict\_\_

---
#### zip

`zip(*iterables)`
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

`\_\_import\_\_()`
