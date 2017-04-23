# Loops

### for

O `for...in` itera sobre um sequência

```python
shopping_list = ['banana', 'apple', 'jelly']

# Usando o método enumerate para pegar a referência do index na iteração
def enumerate_example():
    for index, item in enumerate(shopping_list):
        print(index, item) #0 banana...

enumerate_example()
```

```python
def get_me_range():
    for x in range(10):
        print(x)
```

```python
def getNumber(numero):
    for n in range(100):
        if n is numero:
            print(n, 'e o numero!')
            break  # Sai do loop quando magicNumber é encontrado
        else:
            print('nao e o numero')

getNumber(26)
```


### while

No `while` o comando roda até uma condição ser alcançada

```python
def loopEmX():
    x = 1
    while x <= 3:
        print(x)
        x += 1

loopEmX()
```
