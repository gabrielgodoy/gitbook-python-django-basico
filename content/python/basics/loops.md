# Loops

```python
shopping_list = ['banana', 'apple', 'jelly']

# Usando o método enumerate para pegar a referência do index na iteração
def enumerate_example():
    for index, item in enumerate(shopping_list):
        print(index, item)

enumerate_example()
```

```python
def get_me_range():
    for x in range(10):
        print(x)
```

```python
def get_me_range_delimitators():
    for x in range(4, 10):
        print(x)
```

```python
# Range method => range(start, end, incrementor)

def get_me_range_incrementor():
    for number in range(4, 10, 2):  # 4 6 8
        print(number)

get_me_range_incrementor()
```

```python
# Range method
def get_magic_number(magic_number):
    for n in range(100):
        if n is magic_number:
            print(n, 'is the magic number!')
            break  # Sai do loop quando magicNumber é encontrado
        else:
            print('no')

get_magic_number(26)
```
