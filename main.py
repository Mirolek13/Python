class Humans:
  def __init__(self):
    self.eat = 80
    self.drink = 80
    self.happy = 100
  
  def humanEat(self):
    self.eat += 20

  def humanDrink(self):
    self.drink += 20

  def humanHappy(self):
    self.happy += 30

class Hero(Humans):
  def __init__(self, name, health, power, weapon):
    super().__init__()
    self.name = name
    self.health = health
    self.power = power
    self.weapon = weapon

  def printInfo(self):
    print("Ім`я: ", self.name)
    print("Рівень здоров'я: ", self.health)
    print("Сила удару: ", self.power)
    print("Зброя: ", self.weapon)

  def heroAtack(self, enemy):
    print("Удар! ", self.name, " атакує ", enemy.name, " з силою ", self.power, " використовуючи ", self.weapon)
    enemy.health -= self.power
    print(enemy.name, " похитнувся...")

class Enemy(Humans):
  def __init__(self, name, health, power, weapon):
    super().__init__()
    self.name = name
    self.health = health
    self.power = power
    self.weapon = weapon

  def printInfo(self):
    print("Ім`я: ", self.name)
    print("Рівень здоров'я: ", self.health)
    print("Сила удару: ", self.power)
    print("Зброя: ", self.weapon)

  def enemyAtack(self, enemy):
    print("Удар! ", self.name, " атакує ", enemy.name, " з силою ", self.power, " використовуючи ", self.weapon)
    enemy.health -= self.power
    print(enemy.name, " похитнувся...")

knight = Hero('Герой', 80, 25, 'меч')
enemy1 = Enemy('Враг', 70, 15, 'ніж')

knight.printInfo()
print("Герой йшов по лісу та зустрічає Врага")
enemy1.printInfo()


while knight.health > 0 and enemy1.health > 0:
  knight.heroAtack(enemy1)
  if enemy1.health > 0:
    enemy1.enemyAtack(knight)
    if knight.health <= 0:
      print(enemy1.name, " переможець!")
      enemy1.humanEat()
      enemy1.humanDrink()
      enemy1.humanHappy()
      print("Рівень їжі " + str(enemy1.eat))
      print("Рівень води " + str(enemy1.drink))
      print("Рівень радісті " + str(enemy1.happy))
  else:
    print(knight.name, " переможець!")
    knight.humanEat()
    knight.humanDrink()
    knight.humanHappy()
    print("Рівень їжі " + str(knight.eat))
    print("Рівень води " + str(knight.drink))
    print("Рівень радісті " + str(knight.happy))


    
  
  