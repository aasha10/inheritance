class person (object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname)
        print(self.lname)

class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = student('joey', 'king', 2021)
x.printname()
print(x.graduationyear)