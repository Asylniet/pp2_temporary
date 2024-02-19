class Person:
  def __init__(self, name, iq) :
    self.name = name
    self.hp = 100
    self.iq = iq

  def study(self):
    self.iq += 5

aiza = Person("Aiza", 140)
aiza.study()

print(aiza.iq)
