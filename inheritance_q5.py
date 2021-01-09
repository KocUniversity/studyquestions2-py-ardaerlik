class Animal(object):
  def __init__(self, name):
    self.name = name

class Dog(Animal):
  def __init__(self, name):
    Animal.__init__(self, name)

  def speak(self):
    return self.name + " says WOOF"
            
class Cat(Animal):
  def __init__(self, name):
    Animal.__init__(self, name)
      
  def speak(self):
    return self.name + " says MEOW"


my_dog = Dog("Runner")
my_cat = Cat("Cotton")

print(my_dog.speak())
print(my_cat.speak())