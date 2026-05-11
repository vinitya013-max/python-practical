class Person:
  def __init__(self, name, age=19):
    self.name = name
    self.age = age

p1 = Person("vinit")
p2 = Person("meet", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)
