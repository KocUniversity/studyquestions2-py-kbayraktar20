# Inheritance Q1

def read_file():
  # TODO: extract name, ID, and the score from the file
  with open("input.txt", "r") as file:
    x = file.readlines()

  name = x[0].split()
  ID = x[1][:-1]
  scores_1 = x[2].split()
  scores = []
  for i in scores_1:
    scores.append(int(i))
  
  r_dict = {'name' : name, 'ID': ID, 'scores' : scores}

  return r_dict


class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def __str__(self):
		return "Name: " + self.lastName + ", " + self.firstName + "\n" + "ID: " + self.idNumber

class Player(Person):
  '''
  The __init__ method
    firstName - A string denoting the Person's first name.  
    lastName - A string denoting the Person's last name.
    id - An integer denoting the Person's ID number.
    scores - An array of integers denoting the Person's test scores.
  '''
  def __init__(self, firstName, lastName, idNumber, scores):
    Person.__init__(self, firstName, lastName, idNumber)
    self.scores = scores

  '''
  The calculate method
    Returns one of the characters A, B, C, D 
    denoting the grade of the player.
  '''
  def calculate(self):
    grade = sum(self.scores) / len(self.scores)
    if grade >= 20:
      return "A"
    elif 20 > grade >= 15:
      return "B"
    elif 15 > grade >= 5:
      return "C"
    else:
      return "D"

  '''
  The total_matches method
  Returns how many matches are played by the player.
  '''
  def total_matches(self):
    return len(self.scores)
  
  def __str__(self):
	  return Person.__str__(self)
  

player_dict = read_file()

# TODO: create the Player instance, print it
player = Player(player_dict["name"][0], player_dict["name"][1], player_dict["ID"], player_dict["scores"])
print(player)
# TODO: compute the grade of the player and print it
print("Grade:", player.calculate())
