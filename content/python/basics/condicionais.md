# Condicionais

```python
shopping_list = ['banana', 'apple', 'jelly']


def conditionals(item):
    if shopping_list[0] is item:
        print('getting some ' + shopping_list[0])

    elif shopping_list[2] is item:
        print('getting some ' + shopping_list[2])

    else:
        print('No item found :(')


conditionals('banana')

numbers = [1, 5, 6, 9]


def dont_print_if_numbers():
    for n in range(15):  # range() printa de 0 a 15
        if n in numbers:  # Não dê print caso o número esteja presente na lista 'numbers'
            continue
        print(n)


dont_print_if_numbers()
```
