class Person:
  def __init__(self, name) :
    self.name = name
    self.hp = 100

  def __str__(self) :
    return f'{self.name} has {self.hp} health'
    # return self.name + " has " + self.hp + " health"

  def study(self):
    self.iq += 5

class House:
  def __init__(self, people):
    self.people = people

  def print_people(self) :
    if len(self.people) == 0 :
      print("No people in house")
      return

    for person in self.people :
      print(person)


person1 = Person("Bibatyr")
person2 = Person("Almira")
house = House([person1, person2])

house.print_people()
