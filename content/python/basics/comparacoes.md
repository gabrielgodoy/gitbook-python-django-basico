# Comparações

Diferença entre `is` e `==`

`is` checa por identidade

`a is b` é verdadeiro caso a e b são o mesmo objeto (os dois são armazenados no mesmo endereço na memória)

`==` checa por igualdade de valor

retorna verdadeiro caso os objetos referidos pelas variáveis são iguais em valor 

```python
1000 is 10 * 100  # False - Não são o mesmo objeto
1000 == 10 * 100  # True - São iguais em valor
```
