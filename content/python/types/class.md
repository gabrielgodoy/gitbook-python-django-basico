# Classes

```python
class Animal:
    def breath(self):
        print('phew')

    def walk(self):
        print('Andando como um animal andaria')
```

```python
class Cat(Animal):  # Cat herda da classe Animal
    life = 7  # variável da classe

    def walk(self):  # Sobrescrevendo o método Animal.walk()
        print('Andando como um gato andaria')

    def meow(self):
        print('meow!')

    def die(self):
        print('Ouch!')
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print('Estou morto')
        else:
            print(str(self.life) + ' life left' if self.life is 1 else str(self.life) + ' lives left')

    # Define um estado inicial para as instâncias dessa classe
    def __init__(self, name):  # Chamado automaticamente quando um novo objeto é criado, como constructors em Javascript
        # variável da instância
        self.name = name  # name é único para cada instância

my_cat = Cat('Puffy')  # Cria uma nova instância
print(my_cat.name)  # Puffy

my_cat.meow()  # meow!
my_cat.die()  # Ouch!
my_cat.walk()  # Ouch!
my_cat.breath()  # phew herdado da classe Animal
my_cat.check_life()  # 6 lives left
```
