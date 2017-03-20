# Operadores

## Operadores Matemáticos

`+`   Adiciona dois operadores  `x + y`

`-`   Subtrai operador à direita da esquerda `x - y`

`*`   Multiplica dois operadores `x * y`

`/`   Divide o operador esquerdo pelo direito (sempre resulta em float) `x / y`

`%`   Módulo - restante da divisão do operador esquerdo pelo direito `x % y` (restante de x / y)

`//`  Floor division - divisão que resulta em número inteiro ajustado para a esquerda na linha de número `x // y`

`**`  Exponente - operador esquerdo elevado à potência da direita `x ** y` (x à potência de y)

```python
x = 15
y = 4

# Output: x + y = 19
print('x + y =', x + y)

# Output: x - y = 11
print('x - y =', x - y)

# Output: x * y = 60
print('x * y =', x * y)

# Output: x / y = 3.75
print('x / y =', x / y)

# Output: x // y = 3
print('x // y =', x // y)

# Output: x ** y = 50625
print('x ** y =', x ** y)
```

## Operadores de comparação
`>`   Maior que - Verdadeiro se o operador esquerdo é maior que o direito `x > y`

`<`   Menos que - Verdadeiro se o operador esquerdo for menor que o direito `x < y`

`==`  Igual a - Verdadeiro se ambos os operadores forem iguais `x == y`

`!=`  Diferente de - Verdadeiro se os operadores não são iguais `x != y`

`>=`  Maior ou igual a - Verdadeiro se o operador esquerdo for maior ou igual ao direito `x >= y`

`<=`  Menor ou igual a - Verdadeiro se o operador esquerdo for menor ou igual ao direito `x <= y`

```python
x = 10
y = 12

# Output: x > y is False
print('x > y  is', x > y)

# Output: x < y is True
print('x < y  is', x < y)

# Output: x == y is False
print('x == y is', x == y)

# Output: x != y is True
print('x != y is', x != y)

# Output: x >= y is False
print('x >= y is', x >= y)

# Output: x <= y is True
print('x <= y is', x <= y)
```

## Operadores Lógicos
`and` True se ambos os operadores forem verdadeiros `x e y`

`or`  True se qualquer um dos operadores for verdadeiro `x ou y`

`not` True se o operador é falso (complementa o operador) `não x`

```python
x = True
y = False

# Output: x and y is False
print('x and y is', x and y)

# Output: x or y is True
print('x or y is', x or y)

# Output: not x is False
print('not x is', not x)
```

## Comparações

Diferença entre `is` e `==`

`is` checa por identidade

`a is b` é verdadeiro caso a e b são o mesmo objeto (os dois são armazenados no mesmo endereço na memória)

`==` checa por igualdade de valor

retorna verdadeiro caso os objetos referidos pelas variáveis são iguais em valor 

```python
1000 is 10 * 100  # False - Não são o mesmo objeto
1000 == 10 * 100  # True - São iguais em valor
```
