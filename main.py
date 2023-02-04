from random import randint






def happy(func):
  def wrapper():
    print('I am happy')
    func()
  return wrapper

def hungry(func):
  def wrapper():
    print('I am not hungry')
    func()
  return wrapper

def game(func):
  def wrapper():
    print('I am playing')
    func()
  return wrapper

def buy(func):
  def wrapper():
    print('I buy car')
    func()
  return wrapper

def study(func):
  def wrapper():
    print('I study')
    func()
  return wrapper

def car(func):
  def wrapper():
    print('I drive')
    func()
  return wrapper

def eat(func):
  def wrapper():
    print('I am eatting')
    func()
  return wrapper

def sad(func):
  def wrapper():
    print('I am sad')
    func()
  return wrapper

def read(func):
  def wrapper():
    print('I read a book')
    func()
  return wrapper

def sit(func):
  def wrapper():
    print('I am sitting')
    func()
  return wrapper

@happy
@hungry
@game
@buy
@study
@car
@eat
@sad
@read
@sit
def human():
  print('I am human')

human()




















# try:
#   name = input("What is your name? ")
#   n = name.islower()
#   if n == True:
#     print("Your name is " + name)
#   if n == False:
#     raise NameError
#   a = int(input("A: "))
#   sign = input("Sign: ")
#   b = int(input("B: "))
#   if sign == "/" and b == 0:
#     raise ZeroDivisionError
#   if sign != '+' and sign != '-' and sign!='*' and sign!='/':
#     raise Warning
#   elif sign == '+':
#     print(f"{a} + {b} = {a+b}")
#   elif sign == '-':
#     print(f"{a} - {b} = {a-b}")
#   elif sign == '*':
#     print(f"{a} * {b} = {a*b}")
#   elif sign == '/':
#     print(f"{a} / {b} = {a/b}")
# except ValueError:
# 	print('You need to input digits!')
# except ZeroDivisionError:
# 	print('Go to school')
# except Warning:
# 	print('Unknown sign')
# except NameError:
#   print("Error, write your name in letters")
# except:
# 	print('Error!')





















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
    