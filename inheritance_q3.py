# Inheritance Q3

class A(object):
  def one(self):
    return 'A'

  def two(self):
    return 'B'
 
class B(A):
  def two(self):
    return self.one()

obj1 = A()
obj2 = B()

print(obj1.two(), obj2.two())