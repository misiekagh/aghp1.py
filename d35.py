PI=3.1415

class Figure:
    def __init__(self, da, db):
        self.da=da
        self.db=db

    def perim(self):
        raise NotImplemented

    def area(self):
        raise NotImplemented

class Rect(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def perim(self):
        return 2*(self.da+self.db)

    def area(self):
        return self.da*self.db

class Solid:
    def __init__(self, dx, dy, dz):
        self.dx=dx
        self.dy=dy
        self.dz=dz

    def vol(self):
        raise NotImplemented

    def area(self):
        pass

class Cube(Solid):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    @property
    def vol(self):
        return self.dx*self.dy*self.dz

a=Rect(4,8)
print(a.perim())
print(a.area())
b=Cube(3,4,5)
print(b.vol)
