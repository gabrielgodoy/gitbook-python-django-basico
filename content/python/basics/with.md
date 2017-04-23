# Usando o `with`

```python
# O with vai automaticamente fechar o arquivo depois que o bloco de código rodar

with open('output.txt', 'w') as file:
    file.write('Hi there!')
```

Usar o `with` garante que um recurso foi 'limpo' quando o código que o utiliza termina de rodar.
