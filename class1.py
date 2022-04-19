# class1.py

class person:

    def __init__(self):
        self.name = "default name"

    def print(self):
        print("My name is {0}".format(self.name))

p1 = person()
p2 = person()
p1.name = "test"
p1.print()
p2.print()

person.title = "ner title"
print(p1.title)
print(p2.title)
print(person.title)

p1.age = 30
print(p1.age)
print(p2.age)