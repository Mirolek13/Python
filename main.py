from random import randint
# class Student:
# 	def __init__(self, name):
# 		self.name = name
# 		self.gladness = 0
# 		self.progress = 0
# 		self.alive = True
# 	def study(self):
# 		self.progress += 20
# 		self.gladness -= 10
# 		print('Study time')
# 	def chill(self):
# 		self.gladness += 35
# 		self.progress -= 8
# 		print('Chill time')
# 	def sleep(self):
# 		self.gladness += 4
# 		print('Sleep time')
# 	def say_hello(self):
# 		print('Hello!')
# 	def live(self):
# 		live_cube = randint(1,4)
# 		if live_cube == 1:
# 			self.study()
# 		elif live_cube == 2:
# 			self.chill()
# 		elif live_cube == 3:
# 			self.sleep()
# 		elif live_cube == 4:
# 			self.say_hello()
# 		self.final()
# 	def final(self):
# 		if self.progress == 100:
# 			print('Amazing! You graduated!')
# 			self.alive = False
# 		elif self.progress < -20:
# 			print('Too bad... You are stupid')
# 			self.alive = False
# 		elif self.gladness < -20:
# 			print('Depression :(')
# 			self.alive = False

# print('Bob\'s life')
# obj1 = Student('Bob')
# for i in range(365):
# 	if obj1.alive == False:
# 		break
# 	obj1.live()

# print('Jane\'s life')
# obj2 = Student('Jane')
# for i in range(365):
# 	if obj2.alive == False:
# 		break
# 	obj2.live()

# class University:
# 	def __init__(self, title):
# 		self.specialization = 'None'
# 		self.address = 'None'
# 		self.title = title
# 		self.descriptopn = 'None'
# 	def study(self, Student):
# 		print(Student.name, 'is studying')
# 	def pay_for_study(self, Mother):
# 		print(Mother.name,'paid for study')

# class Mother:
# 	def __init__(self, name):
# 		self.name = name
# 	def argue(self):
# 		print("I'm angry!!!")
		
# print('Bob\'s life')
# obj1 = Student('Bob')
# for i in range(365):
# 	if obj1.alive == False:
# 		break
# 	obj1.live()

# print('Jane\'s life')
# obj2 = Student('Jane')
# for i in range(365):
# 	if obj2.alive == False:
# 		break
# 	obj2.live()

# univer = University('Oxford')
# univer.study(obj2)


# mom = Mother('Chloe')
# mom.argue()
# univer.pay_for_study(mom)

class Pet:
  def __init__(self, name):
    self.name = name
    self.health = 100
    self.hungry = 60
    self.happy = 60
    self.alive = True
  def game(self, PetPeople):
    self.hungry -= 15
    self.happy += 25
    PetPeople.happy += 20
    print("Pet is happy")
  def petEat(self, PetPeople):
    self.hungry += 20
    self.happy += 5
    PetPeople.happy += 5
    print("Pet isnt hungry")
  def petFight(self, PetPeople):
    livePet = randint(1, 2)
    if livePet == 1:
      self.health -= 40
      self.hungry -= 30
      self.happy -= 30
      PetPeople.happy -= 35
      print("Pet didnt win")
    elif livePet == 2:
      self.health -= 20
      self.hungry -= 20
      self.happy -= 5
      PetPeople.happy -= 30
      print("Pet won")
  def petMedic(self, PetPeople):
    self.health += 60
    self.hungry -= 5
    self.happy += 10
    PetPeople.happy += 35
    print("Pet have more health")
  def liveOfPet(self):
    if self.happy <= 20:
      print("Pet depression")
      self.alive = False
    elif self.health <= 10:
      print("Pet is died")
      self.alive = False
    elif self.hungry <= 10:
      print("Pet very hungry and died")
      self.alive = False
    elif self.hungry >= 75 and self.happy >= 75:
      print("Pet is big and go to other way")
      self.alive = False
  def petLiveFun(self, owner):
    petrandom = randint(1, 4)
    if petrandom == 1:
      self.game(owner)
    elif petrandom == 2:
      self.petEat(owner)
    elif petrandom == 3:
      self.petFight(owner)
    elif petrandom == 4:
      self.petMedic(owner)
    self.liveOfPet()
    
class PetPeople:
  def __init__(self, peopleName):
    self.name = peopleName
    self.happy = 80

owner = PetPeople("Dima")
obj3 = Pet("Vitya")
for i in range(365):
  if obj3.alive == False:
    break
  obj3.petLiveFun(owner)









