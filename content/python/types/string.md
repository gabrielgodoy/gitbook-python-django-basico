# Strings

Existem dois tipos de string em Python. O tradicional tipo `str` e o novo tipo `unicode`.

Se você escreve uma string literal sem o `u` na frente você define uma string do tipo tradicional, que armazena caracteres de 8-bit, e se você coloca o `u` na frente você recebe o novo tipo de string em unicode, que consegue armazenar qualquer caracter Unicode.

```python
oldString = 'ok'
newString = u'ok'
```

## Raw strings

`r'raw string'` diz ao Python para não interpretar nenhum caracter especial dentro da string

É útil para definir caminhos, pois evita uma interpretação indesejada do Python em uma string

```python
my_raw_variable = r'./this/is/a/path'
```
