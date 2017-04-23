## Operadores especiais

### Operadores de identidade

`is` e `is not` são operadores de identidade. Eles são usados para verificar se dois valores (ou variáveis) estão localizados na mesma parte da memória. Duas variáveis que são iguais não significa que sejam idênticas.

Diferença entre `is` e `==`

`is` checa por identidade

`a is b` é verdadeiro caso a e b são o mesmo objeto (os dois são armazenados no mesmo endereço na memória)

`==` checa por igualdade de valor

retorna verdadeiro caso os objetos referidos pelas variáveis são iguais em valor

```python
1000 is 10 * 100  # False - Não são o mesmo objeto
1000 == 10 * 100  # True - São iguais em valor
```

### Operadores de Associação

`in` e `not in` são os operadores de associação em Python. Eles são usados para testar se um valor ou variável é encontrado em uma seqüência (seqüência de caracteres, lista, tuple, conjunto e dicionário).

{% hint style='info' %}
Em um dicionário nós podemos somente testar pela presença da chave, não o valor.
{% endhint %}

```python
x = 'Hello world'
y = {1:'a',2:'b'}

print('H' in x) # True

print('hello' not in x) # True

print(1 in y) # True

print('a' in y) # False
```
