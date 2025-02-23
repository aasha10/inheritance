class person (object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee (person):
    def __init__(self, name, idnumber, salary, position):
        self.salary = salary
        self.position = position
        person.__init__(self, name, idnumber)

a = employee('penguin', 20210401, 15000, 'intern')

a.display()
