# Lidando com Exceções

Algumas Exceções nativas (https://docs.python.org/2/library/exceptions.html)

```python
# SyntaxError significa Código escrito de maneira errada
numero_favorito = int(in put('Qual seu número favorito?\n')) # SyntaxError por causa do "in put"

# ValueError: O script esperava um número, mas usuário inseriu unma string
# ZeroDivisionError: É exibido quando o segundo argumento da divisão ou módulo é zero
```

## Lidando com erros

```python
# Execute o código várias vezes, até que o usuário insira um número corretamente
# Se um número é inserido corretamente, dê um break do loop

while True:
    try:
        numero_favorito = int(input('Qual seu numero favorito?\n'))
        print(18 / numero_favorito)
        break
    except ValueError:
        print('O input precisa ser um numero')
    except ZeroDivisionError:
        print('Nao escolha zero')

    # Para lidar com TODAS as exceções
    except:
        print('Aconteceu um erro desconhecido')

    # Execute essa linha abaixo en todos os casos
    # Essa linha executa todas as vezes no loop
    finally:
        print('loop completado')
```
