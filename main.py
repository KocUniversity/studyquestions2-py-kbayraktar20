class House(object):

  def __init__(self, sigil, motto, name):
    self.sigil = sigil
    self.motto = motto
    self.name = name
    self.allies = []
    self.enemies = []

  def __str__(self):
    return f"Our sigil is a {self.sigil} and our motto is \"{self.motto}\"."

  def speak(self):
    return self.motto

  def show(self):
    return self.sigil

  def set_motto(self, motto):
    self.motto = motto 
  
  def set_sigil(self, sigil):
    self.sigil = sigil
  
  def make_an_alliance(self, house):
    self.allies.append(house.name)
    house.allies.append(self.name)
    if house.name in self.enemies:
      self.enemies.remove(house.name)
      house.enemies.remove(self.name)

  def go_to_war(self, house):
    self.enemies.append(house.name)
    house.enemies.append(self.name)
    if house.name in self.allies:
      self.allies.remove(house.name)
      house.allies.remove(self.name)
    for house in houses2:
      if house.enemies:
        a = ", ".join(house.enemies)
        print(f"House {house.name} is in war against House {a}.")

  def make_peace(self, house):
    self.enemies.remove(house.name)
    house.enemies.remove(self.name)

  def conspire_against(self, houses):
    for i in houses:
      self.enemies.append(i.name)
    for i in houses:
      i.enemies.append(self.name)
    for house in houses:
      if house.name in self.allies:
        self.allies.remove(house.name)
        house.allies.remove(self.name)
      for n in houses2:
        if n.enemies:
          a = ", ".join(n.enemies)
          print(f"House {n.name} is in war against House {a}.")


Stark = House("direwolf", "Winter Is Coming", "Stark")
Arryn = House("falcon", "As High As Honor", "Arryn")
Lannister = House("golden lion", "A Lannister Always Pays His Debts", "Lannister")
Targaryen = House("three-headed dragon", "Fire and Blood", "Targaryen")
Greyjoy = House("golden kraken", "We Do Not Sow", "Greyjoy")
Baratheon = House("crowned black stag", "Ours Isthe Fury", "Baratheon")
Martell = House("red sun pierced by a golden spear", "Unbowed, Unbent, Unbroken", "Martell")
Tully = House("silver trout", "Family, Duty, Honor", "Tully")
Tyrell = House("golden rose", "Growing Strong", "Tyrell")

houses2 = [Stark, Arryn, Lannister, Targaryen, Greyjoy, Baratheon, Martell, Tully, Tyrell]

Stark.make_an_alliance(Arryn)
Stark.go_to_war(Arryn)
Stark.go_to_war(Tully)
Stark.make_peace(Tully)
Stark.conspire_against([Greyjoy, Lannister, Targaryen])