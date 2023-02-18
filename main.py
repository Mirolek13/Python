from random import randint















class Literatura:
  def __init__(self, title):
    self.autor = 'None'
    self.title = title
    self.genre = 'None'
  def read(self):
    print(self.title + " is being read")

class Book(Literatura):
  def __init__(self, title):
    super().__init__(title)
    self.pages = 0
  def read(self):
    super().read()
    print('I like to read ' + self.title)
  def write(self):
    print('I write fanfic of ', self.title)

class Magazine(Literatura):
  def __init__(self, title):
    super().__init__(title)
    self.pages = 0
  def read(self):
    super().read()
    print('I like to read ' + self.title)
  def write(self):
    print('I write of ', self.title)

magazine1 = Magazine("SuperMarket")
magazine1.read()
magazine1.write()

book1 = Book('Harry Potter')
book1.read()
book1.write()
    
    










    

# try:
#   def decor(func):
#     def wrapper1():
#        print("") 
#   def count():
#     name = input("What is your name? ")
#     n = name.islower()
#     if n == True:
#       print("Your name is " + name)
#     if n == False:
#       raise NameError
#     a = int(input("A: "))
#     sign = input("Sign: ")
#     b = int(input("B: "))
#     if sign == "/" and b == 0:
#       raise ZeroDivisionError
#     if sign != '+' and sign != '-' and sign!='*' and sign!='/':
#       raise Warning
#     elif sign == '+':
#       print(f"{a} + {b} = {a+b}")
#     elif sign == '-':
#       print(f"{a} - {b} = {a-b}")
#     elif sign == '*':
#       print(f"{a} * {b} = {a*b}")
#     elif sign == '/':
#       print(f"{a} / {b} = {a/b}")
#     except SyntaxError:
#       print('You need to input digits!')
#     except ZeroDivisionError:
#       print('Go to school')
#     except Warning:
#       print('Unknown sign')
#     except NameError:
#       print("Error, write your name in letters")
#     except:
#       print('Error!')






















    