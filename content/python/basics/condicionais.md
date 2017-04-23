# Condicionais

### `if`, `elif` e `else`

```python
def verificaVelocidade(velocidade):
  limite_velocidade = 110
  if velocidade > limite_velocidade:
    multa = (velocidade - limite_velocidade) * 5
    print('Multado em ' + str(multa) + ' reais')
    return multa
  print('Velocidade aceitavel')

verificaVelocidade(120); # Multado em 50 reais
```

```python
lista_compra = ['banana', 'apple', 'jelly']

def verificaItem(item):
    if lista_compra[0] is item:
        print('Pegando o item ' + lista_compra[0])

    elif lista_compra[2] is item:
        print('Pegando o item ' + lista_compra[2])

    else:
        print('Nenhum item encontrado :(')

verificaItem('banana')
```
