import math
class Shape:

  def __init__(self, color='black', filled=False):
    self.color = color
    self.filled = filled

  def get_color(self):
    # TODO
    return self.color

  def set_color(self, color):
    # TODO
    self.color = color

  def get_filled(self):
    # TODO
    return self.filled

  def set_filled(self, filled):
    # TODO
    self.filled = filled

class Rectangle(Shape):

  def __init__(self, height, width):
    Shape.__init__(self)
    self.height = height
    self.width = width

  def get_height(self):
    # TODO
    return self.height

  def set_length(self, height):
    # TODO
    self.height = height

  def get_width(self):
    # TODO
    return self.width

  def set_width(self, width):
    # TODO
    self.width = width

  def get_area(self):
    # TODO
    return self.height * self.width

  def get_perimeter(self):
    # TODO
    return 2 * (self.height + self.width)


class Circle(Shape):
  def __init__(self, radius):
    Shape.__init__(self)
    self.radius = radius

  def get_radius(self):
    # TODO
    return self.radius

  def set_radius(self, radius):
    # TODO
    self.radius = radius

  def get_area(self):
    # TODO
    return math.pi * (self.radius**2)

  def get_perimeter(self):
    # TODO
    return 2 * math.pi * self.radius

r1 = Rectangle(10.5, 2.5)

print("Area of rectangle r1:", r1.get_area())
print("Perimeter of rectangle r1:", r1.get_perimeter())
print("Color of rectangle r1:", r1.get_color())
print("Is rectangle r1 filled? ", r1.get_filled())
r1.set_filled(True)
print("Is rectangle r1 filled? ", r1.get_filled())
r1.set_color("orange")
print("Color of rectangle r1:", r1.get_color())

c1 = Circle(12)

print("\nArea of circle c1:", format(c1.get_area(), "0.2f"))
print("Perimeter of circle c1:", format(c1.get_perimeter(), "0.2f"))
print("Color of circle c1:", c1.get_color())
print("Is circle c1 filled? ", c1.get_filled())
c1.set_filled(True)
print("Is circle c1 filled? ", c1.get_filled())
c1.set_color("blue")
print("Is circle c1 filled? ", c1.get_filled())
print("Color of circle c1:", c1.get_color())