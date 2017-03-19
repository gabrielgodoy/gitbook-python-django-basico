# Dicionários

Dicionários são mutáveis

```python
myDictionary = {
    'apple': 'red round fruit',
    'orange': 'orange round fruit'
}

print(myDictionary['apple'])
```

## Loop em dicionários

```python
def loopMyDict(dictionary):
    # para cada item em items(), loop na chave e no valor
    for key, value in dictionary.items():
        print(key, 'is', value);

loopMyDict(myDictionary)
```
