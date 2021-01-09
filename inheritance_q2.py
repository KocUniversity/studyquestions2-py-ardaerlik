class Polygon:
  def __init__(self, no_of_sides):
    self.n = no_of_sides
    self.sides = [0 for i in range(no_of_sides)]

  def inputSides(self):
    # TODO

  def dispSides(self):
    # TODO

class Triangle(Polygon):
  def __init__(self):
    Polygon.__init__(self, 3)

  def findArea(self):
    # TODO


t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()
