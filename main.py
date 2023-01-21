from random import randint
class Student:
  def characteristicsPeople(self, name):
    self.name = "Dima"
    self.study = 0
    self.happy = 100
    self.money = 5
  def studyPeople(self):
    self.study += 10
    self.happy -= 20
    self.money += 20
  def happyPeople(self):
    self.happy += 20
    self.study -= 15
    self.money -= 10
  def sleepPeople(self):
    self.happy += 10
  def shop(self):
    if self.money >= 20:
      self.money -= 20