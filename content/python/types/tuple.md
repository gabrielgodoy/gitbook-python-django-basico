# Tuples

Tuple é uma sequência de `objetos imutáveis`

Diferente de Lists, Tuples não podem ser mudados

Eles são evolvidos por parentêses, e listas por colchetes

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
