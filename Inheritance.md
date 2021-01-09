## Q1: Person and Player

You are given two classes, `Person` and `Player`, where `Person` is the parent class and `Player` is the child class for a basketball player.

Complete code for the `Person` and `Player` classes in "inheritance_q1.py". `Player` inherits all the properties of the `Person` class. **Hint:** Use the `__init__` method of `Person`to initialize the `Player` by not repeating the same code. In addition, `Player` has another attribute called `scores` that is a list of integers to represent the scores of the `Player`.

Then, complete the `calculate` method that calculates the average for the `Player` and returns a grade, that is a character, according to that average:

> A: points_avg >= 20
  B: 20 > points_avg >= 15
  C: 15 > points_avg >= 5
  D: 5 > points_avg

Moreover, you need to complete the `total_matches` method, which will simply return how many matches that player has played.

### Input Format

Start by implementing the `read_file` function to read the required inputs for our player.

The first line contains the `firstName` and the `lastName` seperated by a space. The second line contains `idNumber`. The third line consists of space-separated integers for the `scores` of the `Player`.

In order to read a text a file line by line, you first need to open it in read mode, and then you can use [`readlines` method of the File module] (https://docs.python.org/3/tutorial/inputoutput.html). Check out the [`split` method for strings](https://docs.python.org/3/library/stdtypes.html#str.split) to tokenize the line into elements separated by space.

### Input/Output

For a simple output like this in the file:

> Kobe Bryant
  8134197
  27 36 15 42

Your output should be as follows:

> Name: Kobe, Bryant
  ID: 8134197
  Grade: A


## Q2: Polygon and Triangle

A polygon is a closed figure with 3 or more sides. We have a class called `Polygon` defined in "inheritance_q2.py" file. We will extend this `Polygon` class to `Triangle`. You will first get the polygon sides as input from the user, and then display it. Then, complete the area function of the triangle function.

> Enter side 1 : 3
  Enter side 2 : 4
  Enter side 3 : 5
  Side 1 is 3.0
  Side 2 is 4.0
  Side 3 is 5.0
  The area of the triangle is 6.00


## Q3: Digging into Inheritance

What is the output for the code in the "inheritance_q3.py"? Why is this code working?

## Q4: Shape Magic

Complete the class functionality given in the "inheritance_q4.py" file to create `Rectangle` and `Circle` as sublclasses of the `Shape` class.

When you run your code with the example case given below, you should get the following output:

> Area of rectangle r1: 26.25
  Perimeter of rectangle r1: 26.0
  Color of rectangle r1: black
  Is rectangle r1 filled ?  False
  Is rectangle r1 filled ?  True
  Color of rectangle r1: orange

  Area of circle c1: 452.39
  Perimeter of circle c1: 75.40
  Color of circle c1: black
  Is circle c1 filled ?  False
  Is circle c1 filled ?  True
  Color of circle c1: blue


## Q5: Having many forms?

Consider this code segment:

```
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

```

Here you see that `Dog` and `Cat` are subclasses of `Animal` class. If yoy check the example case given, you see that they speak differently. Why is that and what is this concept called?
