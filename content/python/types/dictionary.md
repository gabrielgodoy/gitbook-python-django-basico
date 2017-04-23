# Dicionários

Dicionários são `mutáveis` (https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

```python
myDictionary = {
    'maca': 'fruta redonda e vermelha',
    'laranja': 'fruta redonda e laranja'
}

print(myDictionary['maca']) # 'fruta redonda e vermelha'
```

## Loop em dicionários

```python
herois = {
    'batman': 'Bruce Wayne',
    'superman': 'Clark Kent',
    'flash': 'Barry Allen'
}

def loopMyDict(dictionary):
    # Para cada item em dictionary.items()
    for key, value in dictionary.items(): #loop na chave e no valor
        print(key, 'is', value);

loopMyDict(herois)
```

##Alguns Métodos

```python
# Inicia um Dicionário
dicio = {}
herois = {'batman': 'Bruce Wayne', 'superman': 'Clark Kent', 'flash': 'Barry Allen'}

# Inserindo um item novo ao dicionário
herois['wonder woman'] = 'Diana'

# Remoção
herois.pop('wonder woman')
del herois['batman']

# Alterando um item já existente do dicionário
herois['wonder woman'] = 'Diana Princess'

# Verificando existência de item no dicionário
'aquaman' in herois # False
'superman' in herois # True

# Listando todas as chaves do dicionário
list(herois.keys())

# Ordenando as chaves do dicionário
sorted(herois.keys())
```
