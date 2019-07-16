class Zwierz:
    def __init__(self,name,legs):
        self.name=name
        self.legs=legs

    def sound(self, snd):
        self.sound=snd

class Chick(Zwierz):
    def __init__(self, name, legs):
        super().__init__(name, legs)

class Dog(Zwierz):
    def __init__(self, name, legs):
        super().__init__(name,legs)

a=Chick('AAA', 4)
a.sound('Buuu')

print(a.__dict__)

