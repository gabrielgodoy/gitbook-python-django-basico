# Strings

`r'raw string'` diz a uma string para não interpretar nenhum caracter especial

Interpreta como a string é, não tente parsear nada de especial no meio dessa string

É útil para definir caminhos, para evitar uma interpretação indesejada do Python em uma string 

```python
my_raw_variable = r'./this/is/a/path'
```

Existem dois tipos de string em Python. O tradicional tipo `str` e o novo tipo unicode.

Se você escreve uma string literal sem o `u` na frente você define uma string do tipo tradicional, que armazena caracteres de 8-bit, e se você coloca o `u` na frente você recebe o novo tipo de string em unicode, que consegue armazenar qualquer caracter Unicode.

```python
oldString = 'ok'
newString = u'ok'
```
