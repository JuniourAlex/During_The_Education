
class User(object):
    def __init__(self, email):
        self.email = email

    def log_in(self):
        print('You logged in')

    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self,name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print (f'attacking with {self.power}')

    def email(self):
        return (f'Email is {self.email}')

class Archer(User):
    def __init__(self, name, arrows, email):
        super().__init__(email)
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'Arrows are left {self.arrows}')

    def email(self):
        return f'Email is {self.email}'

    def __iter__(self):
        self.x = 1
        return self

    def __call__(self):
        return 'Hi, world'

wizard1 = Wizard ('Alex',60, 'Alex@mail.ru')
archer1 = Archer('Andrew',300,'Geometry@mail.ru')
print(wizard1.log_in())
print(wizard1.attack())
print(archer1())

