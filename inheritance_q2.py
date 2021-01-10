class Polygon:
  def __init__(self, no_of_sides):
    self.n = no_of_sides
    self.sides = [0 for i in range(no_of_sides)]

  def inputSides(self):
    for i in range(len(self.sides)):
      self.sides[i] = float(input("Enter side " + str(i+1) + ": " ))
    return self.sides

  def dispSides(self):
    for i in range(len(self.sides)):
      print("Side " + str(i+1) + " is " + str(self.sides[i]))

class Triangle(Polygon):
  def __init__(self):
    Polygon.__init__(self, 3)

  def findArea(self):
    # TODO
    print(f"The area of the triangle is {self.sides[0]*self.sides[1]/2}.")


t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()
