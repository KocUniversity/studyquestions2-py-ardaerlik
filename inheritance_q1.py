# Inheritance Q1

def read_file():
  # TODO: extract name, ID, and the score from the file
  

  r_dict = {'name' : name, 'ID': ID, 'scores' : scores}

  return r_dict


class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def __str__(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Player(Person):
  '''
  The __init__ method
    firstName - A string denoting the Person's first name.  
    lastName - A string denoting the Person's last name.
    id - An integer denoting the Person's ID number.
    scores - An array of integers denoting the Person's test scores.
  '''


  '''
  The calculate method
    Returns one of the characters A, B, C, D 
    denoting the grade of the player.
  '''


  '''
  The total_matches method
    Returns how many matches are played by the player.
  '''

  pass


player_dict = read_file()

# TODO: create the Player instance, print it

# TODO: compute the grade of the player and print it


