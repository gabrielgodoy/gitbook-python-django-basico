# Tuples

Tuple é uma sequência de `objetos imutáveis`

Diferente de Listas, os items de um Tuple não podem ser mudados

Eles são envolvidos por parênteses `()`

```python
# Tuples
iAmATuple = (1, 2, 3)
print(type(iAmATuple))  # <class 'tuple'>

# Loop em items tuple
for number in iAmATuple:
    print(number)

# Para escrever um tuple com um único valor, ele precisa terminar com vírgula também
tupleWithSingleItem = (50,)
```
