import ps
import gear
from random import randint
spells_learned = ["Heal", "Fire"]

def minor_healing():
  if ps.magic >= 10:
    healed = randint(1,35) + (ps.magic_power *0.65)
    ps.hp += healed
    ps.magic -= 10
    input("You healed " + str(healed) + " HP!")
    print(str(ps.magic) + " Magic Remaining")
  elif ps.magic < 10:
    print("You don't have enough magic!")

def minor_fire():
  if ps.magic >= 10:
    fired = randint(1,100)
    if fired <= 25:
      print("Your fire did nothing.")
      ps.magic -= 10
      print(str(ps.magic) + " Magic Remaining")
      return 0
    else:
      firedamage = randint(1,35) + (ps.magic_power *0.65)
      ps.magic -=10
      print("You dealt " + str(firedamage) + "!")
      print(str(ps.magic) + " Magic Remaining")
      return firedamage
  elif ps.magic < 10:
    print("You don't have enough magic!")