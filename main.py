from random import randint



try:
  name = input("What is your name? ")
  n = name.islower()
  if n == True:
    print("Your name is " + name)
  if n == False:
    raise NameError
  a = int(input("A: "))
  sign = input("Sign: ")
  b = int(input("B: "))
  if sign == "/" and b == 0:
    raise ZeroDivisionError
  if sign != '+' and sign != '-' and sign!='*' and sign!='/':
    raise Warning
  elif sign == '+':
    print(f"{a} + {b} = {a+b}")
  elif sign == '-':
    print(f"{a} - {b} = {a-b}")
  elif sign == '*':
    print(f"{a} * {b} = {a*b}")
  elif sign == '/':
    print(f"{a} / {b} = {a/b}")
except ValueError:
	print('You need to input digits!')
except ZeroDivisionError:
	print('Go to school')
except Warning:
	print('Unknown sign')
except NameError:
  print("Error, write your name in letters")
except:
	print('Error!')





















#class Student:
#  def characteristicsPeople(self, name):
#    self.name = "Dima"
#    self.study = 0
#    self.happy = 100
#    self.money = 5
#  def studyPeople(self):
#    self.study += 10
#    self.happy -= 20
#    self.money += 20
#  def happyPeople(self):
#    self.happy += 20
#    self.study -= 15
#    self.money -= 10
#  def sleepPeople(self):
#    self.happy += 10
#  def shop(self):
#    if self.money >= 20:
#      self.money -= 20




#class Universitet:
#  def init(self, title):
 #   self.title = "Oxford"
    