import spells
import ps
import bad
import gear
import main_menu
from random import randint

def combat(enemy,ename,elevel):
  def defend(enemy,ename,elevel):
    damages = randint(1,34)
    damages = (damages + (damages * (elevel *0.387))) - (ps.defense // elevel)
    print("")
    print("You lost " + str(damages) + " hp.")
    ps.hp = ps.hp - damages
    print(str(ps.hp) + " HP Remaining")
    print("")
    if ps.hp > 0 and enemy > 0:
      input("Press Enter to Attack")
      print("")
      attack(enemy,ename,elevel)
    elif ps.hp < 0:
      print("You died nerd")
      crate()
      return
    elif enemy <= 0:
      print("Jason has made the code wrong if this runs!")
    else:
      print("ERROR")
  def attack(enemy,ename,elevel):
    print("")
    MM = input("""Would you like to use:
  1. Melee
  2. Magic
  """)
    if MM.lower() == "1":
      rng = randint(1,4)
      damage = rng * ps.strength
      enemy = enemy - damage
      print("You attacked the " + ename + " for " + str(damage) + " damage!")
      if enemy > 0:
        input("Press Enter to Defend")
        print("")
        ps.magic += 5
        defend(enemy,ename,elevel)
      elif enemy <= 0:
        ps.magic += 5
        print("You defeated the " + ename + "!")
        xp_Gained = randint(1,15) * 1.75 // (elevel - randint(1,5))
        xp += xp_Gained
        e = ps.level + 1
        arenas()
        while xp >= 1.75**e:
          ps.level += 1
          print("You leveled up! You are now level " + str(ps.level) + "!")
        Gold_added = randint(1,34) * (elevel * 0.46)
        ps.money += Gold_added
        arenas()
      else:
        print("ERROR")
    elif MM.lower() == "2":
      print("""Spells Avavible:""" + str(spells.spells_learned))
      cast = input("What spell would you like to use?")
      cast = cast.lower()
      print("")
      if "heal" in cast:
        spells.minor_healing()
        defend(enemy,ename,elevel)
      elif "fire" in cast:
        enemy = enemy - spells.minor_fire()
        print("The enemy has " + str(enemy) + " Health Left")
        if enemy > 0:
          input("Press Enter to Defend")
          print("")
          ps.magic += 5
          defend(enemy,ename,elevel)
        elif enemy <= 0:
          ps.magic += 5
          print("You defeated the " + ename + "!")
          xp_Gained = randint(1,15) * 1.75 // (elevel - randint(1,5))
        #  ps.xp += xp_Gained
        #  while xp >= 1.75**(ps.level + 1):
        #    ps.level += 1
        #    print("You leveled up! You are now level " + str(ps.level) + "!")
          arenas()
        else:
          print("ERROR")
        input("Press Enter to Defend")
        defend(enemy,ename,elevel)
    else:
      attack(enemy,ename,elevel)
  attack(enemy,ename,elevel)
  
def arenas():
  randenemy = randint(0,18)
  enemy = bad.bad_guys[randenemy]
  ename = bad.bad_names[randenemy]
  elevel = bad.bad_level[randenemy]
  print("")
  input("You are fighting a " + ename + ". Press enter to FIGHT!")
  combat(enemy,ename,elevel)
  
def crate():
  print("")
  input("After leaving the Arena you find your prize by the door. Press Enter to Open")
  Crate = randint(1,2)
  if Crate == 1:
    CArmor = randint(0,6)
    CPiece = randint(1,4)
    if CPiece == 1:
      gear.Head = gear.treasure_armor[CArmor]
      print("")
      input("You equiped a " + gear.tanames[CArmor] + " on your head! (You lost your old head gear) Press Enter to Return to the main menu")
    elif CPiece == 2:
      gear.Legs = gear.treasure_armor[CArmor]
      print("")
      input("You equiped a " + gear.tanames[CArmor] + " on your legs! (You lost your old leg gear) Press Enter to Return to the main menu")
    elif CPiece == 3:
      gear.Torso = gear.treasure_armor[CArmor]
      print("")
      input("You equiped a " + gear.tanames[CArmor] + " on your torso! (You lost your old torso gear) Press Enter to Return to the main menu")
    elif CPiece == 4:
      gear.Feet = gear.treasure_armor[CArmor]
      print("")
      input("You equiped a " + gear.tanames[CArmor] + " on your Feet! (You lost your old foot gear) Press Enter to Return to the main menu")
    main_menu.Main_menu()
  elif Crate == 2:
    CWeapon = randint(0,7)
    gear.RHand = gear.treasure_weapon[CWeapon]
    print("")
    input("You equiped a " + gear.twnames[CWeapon] + " in your hand! (You lost your old weapon) Press Enter to Return to the main menu")
    main_menu.Main_menu()