# IMPORTS
import matplotlib.pyplot as plt
import random

# VARIABLES
startingPopulation = 50000
infantMortalitiy = 25
agriculture = 5
food = 1
disasterChance = 10
fertility_x = 18
fertility_y = 35
totalFood = 0

# LINE GRAPH

x_list = []
y_list = []

# COLORS

color_list = ["red", "orange", "yellow", "green", "blue"]

# PEOPLE DICTIONARY
peopleDict = []

# PERSON CLASS

class Person:
  # CONSTRUCTOR
  # assigns gender, age, and anme variables to each person object
  # the gender is assigned using 0, 1 numbers, 0 is male, 1 is female
  def __init__(self, age):
    self.gender = random.randint(0, 1)
    self.age = age

  # HARVEST
  # if the person is 8 or older, they can make food
  # food is calculated by the number of people above 8 times agriculture 

def harvest(food, agriculture):
  totalFood = 0
  ablePeople = 0

  for person in peopleDict:
    if (person.age >= 8):
      ablePeople +=1 

  totalFood+=ablePeople * agriculture

  if totalFood < len(peopleDict):
    del peopleDict[0: int(len(peopleDict) - totalFood)]
    totalFood = 0

  else: 
    totalFood -= len(peopleDict)

  # REPRODUCE
  # if the person is a female, they reproduce

def reproduce(fertility_x, fertility_y):
  for person in peopleDict:
    if(person.gender == 1):
      if(person.age>fertility_x) and (person.age<fertility_y):
        if random.randint(0, 10) == 1:
            personNew = Person(0)
            peopleDict.append(personNew)

def beginSimulation():
  for counter in range(startingPopulation):
    peopleDict.append(Person(random.randint(0, 80)))

beginSimulation()
yearsCount = 0
years = 0

def runYear(food, agriculture, fertility_x, fertility_y):
  harvest(food, agriculture)
  reproduce(fertility_x, fertility_y)

  for person in peopleDict:
    if person.age > 80:
      peopleDict.remove(person)

    else:
      person.age+=1

  # print(len(peopleDict))

while len(peopleDict) < 100000 and len(peopleDict) > 1:
  runYear(food, agriculture, fertility_x, fertility_y)
  yearsCount +=1 
  years += 1
  
  if(yearsCount==10):
    x_list.append(years)
    y_list.append(len(peopleDict))
    yearsCount = 0

plt.title("Human Simulation")
color = random.choice(color_list)
plt.plot(x_list, y_list, label="Population", color=color)
plt.xlabel("Years")
plt.ylabel("Humans Alive")
plt.legend()
plt.show()

print("The simulation ran for " + str(years) + " years!")
