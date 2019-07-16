PI=3.1415

class Shape:
    def __init__(self, name, sides_cnt=0, *args):
        self.name=name

    def perim(self):
        return sum(args)

    def area(self):
        pass

class Square(Shape):
    def __init__(self, name, w):
        super().__init__(name, 4, w, w, w, w)
        self.w=w

class Cube:
    def __init__(self, side):
        self.side=side

    def volume(self):
        return self.side**3

    def area(self):
        return 6*self.side**2

class Circle:
    def __init__(self, radius):
        self.rad=radius

    def circum(self):
        return 2*PI*self.rad

    def area(self):
        return PI*self.rad**2


figs=[Square(4),Circle(4),Cube(4)]

for f in figs:
    if isinstance(f,Cube):
        print(f.volume())
    else:
        print(f.area())