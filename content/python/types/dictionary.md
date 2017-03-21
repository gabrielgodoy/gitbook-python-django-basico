# Dicionários

Dicionários são `mutáveis` (https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

```python
myDictionary = {
    'apple': 'red round fruit',
    'orange': 'orange round fruit'
}

print(myDictionary['apple']) #'red round fruit'
```

## Loop em dicionários

```python
heroes = {
    'batman': 'Bruce Wayne',
    'superman': 'Clark Kent',
    'flash': 'Barry Allen'
}

def loopMyDict(dictionary):
    # para cada item em dictionary.items()
    for key, value in dictionary.items(): #loop na chave e no valor
        print(key, 'is', value);

loopMyDict(heroes)
```

##Alguns Métodos

```python
#Inicia um Dicionário
dicio = {}
heroes = {'batman': 'Bruce Wayne', 'superman': 'Clark Kent', 'flash': 'Barry Allen'}

#Inserção
heroes['wonder woman'] = 'Diana'

#Remoção
heroes.pop('wonder woman')
del heroes['batman']

#Alteração
heroes['wonder woman'] = 'Diana Princess'

#Verifica existência
'aquaman' in heroes #False
'superman' in heroes #True

#Lista todas as chaves
list(heroes.keys())

#Ordena as chaves
sorted(heroes.keys())
```
