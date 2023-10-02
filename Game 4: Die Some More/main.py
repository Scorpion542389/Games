from random import randint,random
import time
import ps
import os
import other
clear = os.system

items = ["Pumpkin","Key","Wishing Coin","Medecine"]

locations = [other.Field,other.Cave,other.mHouse,other.wishWell,other.Shop]

def rEvent():
  print("BAD THING")
  return


def risk():
  rCheck = random()
  kCheck = random()
  if ps.rng <= kCheck:
    return
  elif ps.rng > kCheck:
    if ps.exposure <= rCheck:
      rEvent()
    elif ps.exposure > rCheck:
      return

def riskAssess():
  if ps.rng == 1:
    ps.risk = 0.00
  elif ps.exposure == 1:
    ps.risk = 1
  else:
    ps.risk = round((ps.exposure) * (1-ps.rng),2)

    
def wait():
  time.sleep(0.5)
  clear('cls')
  waitLength = input("How long (in hours) would you like to wait for? (Max: 10) Type '0' to go back)")
  if waitLength == "0":
    cS()
  elif int(waitLength) > 0 and int(waitLength) <= 10:
    ps.time += int(waitLength) * 100
    e = 0
    while e <= int(waitLength):
      hour()
      e += 1
    cS()
  else:
    print("Try again!")
def eat():
  clear('cls')
  if ps.food > 0:
    ps.food -= 1
    ps.hunger = 0
    response = "Hunger Reset. You have " + str(ps.food) + " pieces of food left."
    hour()
    return response
  elif ps.food <= 0:
    response = "You don't have enough food!"
    return response
def hour():
  ps.hunger += randint(1,10)
  if ps.hunger >= 45:
    ps.bonusK -= 10 + ((ps.hunger-45)/2)
  ps.rng = round((random() + (ps.bonusK/100)),2)
  riskAssess()
  ps.time += 100
  risk()
  cS()
def use():
  item = input("What would you like to use?").lower()
  if item in ps.inventory:
    print("You can't use any items yet. How you get here???")
    cS()
  else:
    print("Item not recognized or not in your inventory!")
    cS()
def explore():
  clear('cls')
  location = locations[randint(0,4)]
  ps.exposure = location.exposure
  ps.location = location.name
  hour()
  cS()
def shop():
  store = other.Store(items[randint(0,3)],items[randint(0,3)],items[randint(0,3)])
  print(store.itemOne)
def unlockHouse():
  return
def wish():
  return
  
  
  




def cS():
  time.sleep(0.75)
  clear('cls')
  karma = ps.rng * 100
  expose = ps.exposure * 100
  risky = ps.risk * 100
  print("""
  Location: {}
  Player Stats:
  Health: {}
  Gold: {}
  Food: {}
  Hunger: {}%
  Exposure: {}%
  Risk: {}%
  Karma: {}%
  Inventory: {}
  Time of Day (Military Time): {}""").format(ps.location,ps.health,ps.gold,ps.food,ps.hunger,expose,risky,karma,ps.inventory,ps.time)
  if ps.location == "Shop":
    print("""
  0. Shop""")
  choice = input("""  
  1. Wait
  2. Explore
  3. Eat
  4. Use Item
  
  Choice: """)
  choice = int(choice)
  if choice == 1:
    wait()
  elif choice == 2:
    explore()
  elif choice == 3:
    print(eat())
    time.sleep(1.5)
    cS()
  elif choice == 4:
    return
  elif choice == 0 and ps.location == "Shop":
    shop()
  else:
    cS()
    
    


def menu():
  #Add Turtle for title later
  start = input("""Would you like to start the game?
  1. Yes
  2. No""")
  if start == "1":
    howToPlay = input("""Do you want to learn how to play?
  1. Yes
  2. No""")
    if howToPlay == "1":
      print("In Progress!")
      cS()
    elif howToPlay == "2":
      cS()
      
cS()