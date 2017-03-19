# Herança de classes

```python
class Plumber:
    def fix_plumbs(self):
        print('Fixing plumb')


class Mario(Plumber):
    slogan = 'Its a me. Mario!'

    def say_hi(self):
        print(self.slogan)

    def move(self):
        print('moving')


class Shroom:
    def eat_shroom(self):
        print('Now i am big')


class BigMario(Mario, Plumber, Shroom):
    pass  # Do nothing


big_mario = BigMario()
big_mario.move()
big_mario.eat_shroom()
big_mario.fix_plumbs()
big_mario.say_hi()
```
