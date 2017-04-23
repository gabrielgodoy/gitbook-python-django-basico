# Herança de classes

```python
class Encanador:
    def consertar_encanamento(self):
        print('Consertando encanamento')

class Mario(Encanador):
    slogan = 'Sou eu. Mario!'

    def falar(self):
        print(self.slogan)

    def mover(self):
        print('movendo')

class Shroom:
    def comer_cogumelo(self):
        print('Agora sou grande')

class BigMario(Mario, Encanador, Shroom): # Subclasse que herda das três outras classes criadas acima
    pass  # Não faça nada

big_mario = BigMario()
big_mario.mover()
big_mario.comer_cogumelo()
big_mario.consertar_encanamento()
big_mario.falar()
```

![Python](../../../assets/images/mario.gif)
