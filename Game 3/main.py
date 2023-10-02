from random import randint
import os
import time
import player
import eventStuff
import bad
import gear
import math
wipe = os.system
wait = time.sleep


def subtractHealth(damage):
  player.hp -= damage
  if player.hp <= 0:
    loser()
  
def addHealth(heal):
  player.hp += heal

def clear(time):
  wait(time)
  wipe('cls')
  wait(1)
  
def stats():
  print("VERSION BETA 0.2.1")
  print("HP: " + str(player.hp))
  print("Gold: " + str(player.gold))
  print("Inventory: " + str(player.inventory))
  print("Turn Number: " + str(player.turns))
  print("Children Kicked: " + str(player.childrenKicked))
  if player.friend == True:
    print("Pet: " + player.dogName)
  if player.carName != "":
    print("Vehicle: " + player.carName)
  print("")

def patchNotes():
  print("")
  print("Added the Pizza Event and the Arena Event!")
  print("Updated the Vending Machine event!")
  print("Added Paper!")
  print("First Winner: fishsticks28")
  print("fishsticks28 added the Vehicle Event!")
  print("")
  print("COMING IN VERSION 0.3")
  print("Armor, (Real) Spells, Fighting")
  print("Items and More Gold!")
  clear(10)
  stats()

def loser():
  print("You lost")
  wait(2)
  print("Loser")
  input(" ")
  loser()
  
def equipt(item, itemName, weapon):
  print("Where would you like to equpit this?")
  if weapon == True:
    where = input("""Where would you like to equipt this item?
  1. Right Hand
  2. Left Hand
  3. Go Back
 """)
    if where == '1':
      item = "E"
  
def use():
  item = input("What would you like to use?")
  if item.lower() == "nice pumpkin" and item in player.inventory:
    print("")
    print("Why would you use such a nice pumpkin?")
    clear(2)
  elif item.lower() == "book" and item in player.inventory:
    print("")
    print("You open the book. It seems to be a message from the developer!")
    patchNotes()
  elif item.lower() == "time spell" and item in player.inventory:
    print("")
    print("You use the time spell to go back in time. It seems to be like this game. But, much harder and older...")
    wait(2)
    print("https://trinket.io/python/dabdc7c90a?outputOnly=true")
    print("Unfortunatly this is all the spell does...")
    wait(8)
  elif item.lower() == "paper" and item in player.inventory:
    print("")
    print("You eat part of the paper and heal 14 HP!")
    wait(3)
    addHealth(14)
    if gear.paperUses == 3:
      print("There is no more paper left")
      wait(3)
      player.inventory.remove("Paper")
    elif gear.paperUses < 3:
      paperUses += 1
  elif item in gear.tanames:
    x = gear.tanames.index(item)
    thing = gear.treasure_armor[x]
    equipt(thing, x, False)
  elif item in gear.twnames:
    x = gear.twnames.index(item)
    thing = gear.treasure_weapon[x]
    equipt(thing, x,True)
  else:
    print("")
    print("I don't know what that item is! Did you spell it right? (Please use correct capitalization)")
    print("")
  if eventStuff.dog == True:
    eventStuff.dog = False
    dog()
  elif eventStuff.orphan == True:
    eventStuff.orphan = False
    orphan()
  elif eventStuff.vending == True:
    eventStuff.vending = False
    vending()
  elif eventStuff.chef == True:
    eventStuff.chef == False
    chef()
  elif eventStuff.pizza == True:
    eventStuff.pizza = False
    pizza()
  elif eventStuff.vehicle == True:
    eventStuff.vehicle = False
    vehicle()
  elif eventStuff.shop == True:
    eventStuff.shop = False
    shop()
  else:
    print("ERROR")

def win():
  clear(0)
  print("You win... Congrats ig")
  input(" ")
  win()
  
def tutorial():
  knowledge = input("""
  Would you like to know how to play?
  1. Yes
  2. No
 """)
  if knowledge == '1':
    clear(1)
    print("All events have at least 2 actions. You select these actions by typing their corrosponding number!")
    wait(2)
    print("After and event or choice the screen will clear. (If the screen clears too quickly please report as a bug)")
    wait(2)
    print("To use an item select 'Use Item' (Usually option #1) then type the item you would like to use")
    wait(2)
    print("To win the game complete 15 turns.")
    wait(2)
    print("If you win a game you are able to add an event or your choice (Must be approved) ONLY IN BETA")
    wait(2)
    print("Please note this game only has a few events so you probably will not win.")
    wait(2)
    print("Please report any bugs to Scorpion54#2389 or Scorpion55#1220 on discord!")
    wait(2)
    print("Have fun! Or don't idc")
    wait(2)
    reh()
  elif knowledge == '2':
    reh()
  else:
    print("Try Again")
    tutorial()

def jail():
  clear(0)
  print("You are sitting in a jail cell. All of your money and stuff has been taken.")
  player.gold = 0
  player.inventory = []
  wait(2)
  print("You have a 15% of being set free. Have fun :D")
  print("(Minus -1% for each child you have kicked!)")
  eventStuff.waitCount = 0
  def freedom():
    free = randint(1,100)
    if eventStuff.waitCount == 3:
      numOne = randint(1,100)
      numTwo = randint(1,100)
      math = input("What is " + str(numOne) + "+" + str(numTwo) + "?")
      if int(math) == (numOne + numTwo):
        print("GoodJob")
      else:
        print("Shame. We will take 1% away from your chance of leaving!")
        player.childrenKicked += 1
        if player.childrenKicked < 0:
          print("You have no chance of leaving Jail. You die in jail.")
    if free < (15-player.childrenKicked):
      print("You have been set free!")
      wait(2)
      reh()
    else:
      input("You sit and wait. (Press Enter to Wait some more)")
      eventStuff.waitCount += 1
      freedom()

def prizes():
  pumpkin = randint(1,2)
  if pumpkin == 1:
    player.gold -= 25
    print("You put the money in the machine and get...")
    wait(2)
    print("a Nice Pumpkin!")
    player.inventory.append("Nice Pumpkin")
    wait(2)
    reh()
  elif pumpkin == 2:
    player.gold -= 25
    stuff = randint(1,2)
    if stuff == 1:
      armor = randint(0,6)
      prize = gear.treasure_armor[armor]
      piece = randint(1,4)
      if piece == 1:
        where = "Head"
        gear.Head = prize
      elif piece == 2:
        where = "Legs"
        gear.Legs = prize
      elif piece == 3:
        where = "Torso"
        gear.Torso = prize
      elif piece == 4:
        where = "Feet"
        gear.Feet = prize
        print("a " + gear.tanames[armor] + "for your " + str(where))
        wait(3)
        print("You put it on immediatly and throw away your old armor.")
      elif stuff == 2:
        weapon = randint(0,6)
        prize = gear.treasure_weapon[weapon]
        piece = randint(1,4)
        if piece == 1:
          where = "Right Hand"
          gear.RHand = prize
        elif piece == 2:
          where = "Left Hand"
          gear.LHand = prize
        print("a " + gear.twnames[armor] + "for your " + str(where))
        wait(3)
        print("You put it on immediatly and throw away your old weapon in that hand.")

def combat(enemy,ename,elevel):
  def defend(enemy,ename,elevel):
    damages = randint(1,34)
    damages = (damages + (damages * (elevel *0.2))) - (player.defense * (elevel/2))
    print("")
    print("You lost " + str(damages) + " hp.")
    player.hp = player.hp - damages
    print(str(player.hp) + " HP Remaining")
    print("")
    if player.hp > 0 and enemy > 0:
      clear(3)
      attack(enemy,ename,elevel)
    elif player.hp < 0:
      print("You died nerd")
      wait(3)
      loser()
    elif enemy <= 0:
      print("Jason has made the code wrong if this runs!")
    else:
      print("ERROR")
  def attack(enemy,ename,elevel):
    print("")
    MM = input("""Would you like to use:
  1. Melee
  2. Heal
  """)
    if MM.lower() == "1":
      rng = randint(1,20)
      damage = rng * player.strength
      crit = randint(1,100)
      if crit >= 80-player.childrenKicked:
        damage *= 2
      enemy = enemy - damage
      print("You attacked the " + ename + " for " + str(damage) + " damage!")
      if enemy > 0:
        clear(3)
        defend(enemy,ename,elevel)
      elif enemy <= 0:
        print("You defeated the " + ename + "!")
        wait(3)
        Gold_added = randint(1,93)
        player.gold += Gold_added
        reh()
      else:
        clear(3)
        defend(enemy,ename,elevel)
    elif MM.lower() == "2":
      health = randint(1,70)
      player.hp += health
      print("You healed " + str(health) + " HP!")
      wait(3)
      defend()
    else:
      attack(enemy,ename,elevel)
  attack(enemy,ename,elevel)
# idea, code for an event is scattered elsewhere, could be trap, could lead to unique item

def chef():
  print("You are hired as a chef at a 5 star resturant.")
  wait(2)
  print("You're first table has: Joe Biden, Donald Trump, Barack Obama, and George Bush")
  wait(2)
  print("They all came back from playing Minecraft together.")
  cook = input("""
  1. Use Item
  2. Cook
  3. Refuse Service
 """)
  if cook == '1':
    eventStuff.chef = True
    use()
  elif cook == '2':
    clear(0)
    burn = randint(1,10)
    if burn < 7:
      clear(1)
      print("You burn their food. But you serve it anyway.")
      wait(2)
      print("They hate it so much that they cancel you in their next Minecraft video.")
      wait(2)
      print("The emotional damage deals 12 damage to you.")
      wait(2)
      print("You are also fired for ruining the food.")
      wait(2)
      subtractHealth(12)
      reh()
    elif burn >= 7:
      clear(1)
      print("You cook the most perfect food you have ever made. It took all of your energy to make the food.")
      wait(2)
      print("They love your food and tip you 2 gold!")
      wait(2)
      print("You decide to quit your job because it's so stressful.")
      wait(2)
      player.gold += 2
      reh()
  elif cook == '3':
    refuse = randint(1,10)
    if refuse < 7:
      clear(1)
      print("You refuse to serve them. They decide to cancel you on their Minecraft video. You ego takes 37 damage.")
      wait(3)
      print("You are also fired")
      wait(2)
      subtractHealth(37)
      reh()
    elif refuse >= 7:
      clear(1)
      print("You refuse to serve them. You are fined 100 gold but you ego heals you 21 HP.")
      wait(3)
      print("You are also fired.")
      wait(2)
      addHealth(21)
      player.gold -= 100
    else:
      print("ERROR")
  else:
    print("Try again")
    chef()
def dog():
  doggie = input("""You see a Dog on the road!
  1. Use Item
  2. Pet
  3. Run
 """)
  if doggie == '1':
    eventStuff.dog = True
    use()
  elif doggie == '2':
    friends = randint(1,10)
    if friends < 5:
      clear(0)
      if player.friend == True:
        print("You pet the dog. But, you already have a dog. " + player.dogName + " gets sad that you didn't pet him...")
        clear(2)
        reh()
      else:
        print("You pet the dog and it likes you! He will stay with you for the rest of the game!")
        player.friend = True
        player.dogName = input("What would you like to name him? ")
        clear(2)
        reh()
    elif friends >= 5:
      clear(0)
      print("The dog bit you dealing 25 damage!")
      subtractHealth(25)
      clear(2)
      reh()
  elif doggie == '3':
    run = randint(1,10)
    if run <= 5:
      clear(0)
      print("You ran away from the dog!")
      clear(2)
      reh()
    elif run > 5:
      clear(0)
      print("The dog caught you and bit you. You lost 25 HP")
      subtractHealth(25)
      clear(2)
      reh()
  else:
    print("Try again")
    dog()
def dysentery():
  sick = randint(1,10)
  if player.immune == True:
    clear(1)
    print("Your immunity saved you from Dysnetary!")
    reh()
  else:
    if sick <= 6:
      print("You got dysentery and...")
      wait(2)
      print("died.")
      wait(1)
      print("nerd")
      return
    elif sick > 6:
      print("You got dysentery and...")
      wait(2)
      print("survived.")
      wait(1)
      print("But you have to pay your medical bills with all your gold and stuff")
      wait(3)
      player.gold = 0
      player.inventory = []
      reh()
def orphan():
  orphanChoice = input("""You come across an Orphan in the road. He seems to be radiating...
  1. Use Item
  2. Punt
  3. Force Labor
 """)
  if orphanChoice == '1':
    eventStuff.orphan = True
    use()
  elif orphanChoice == '2':
    steel = randint(1,10)
    if steel <= 4:
      if player.childrenKicked >= 1:
        clear(1)
        print("You punt the orphan but he is secretly Super Man as a kid.")
        wait(2)
        print("agian")
        wait(2)
        print("Superman puts you in jail.")
        wait(2)
        jail()
      clear(1)
      print("You punt the orphan but he is secretly Super Man as a kid.")
      wait(3)
      print("He kicks you back dealing 53 damage")
      subtractHealth(53)
      player.childrenKicked += 1
      wait(3)
      reh()
    elif steel > 4:
      clear(1)
      print("You punt the child. He is launched across the horizon never to be seen again.")
      wait(3)
      print("You see that some gold fell out of his pockets when you punted him.")
      player.gold += randint(1,150)
      player.childrenKicked += 1
      wait(3)
      reh()
  elif orphanChoice == '3':
    coal = randint(1,10)
    if coal <= 3:
      clear(1)
      print("You force the orphan to go work in the coal mines.")
      wait(3)
      player.perTurn += randint(1,30)
      print("He agrees and now earns you " + str(player.perTurn) + " gold per turn.")
      wait(3)
      reh()
    elif coal > 3:
      clear(1)
      print("You force the orphan to go work in the coal mines.")
      wait(3)
      print("He fights back and hits you with a very poorly photoshopped sword dealing 32 damage.")
      subtractHealth(32)
      wait(3)
      reh()
  else:
    print("Try Again")
    orphan()
def vending():
  machine = input("""You come across a vending machine in the middle of the road. It offers a mysery item for 25 gold!
  1. Use Item
  2. Buy Mysery Item
  3. Punch Machine
  4. Walk Away
 """)
  if machine == '1':
    eventStuff.vending = True
    use()
  elif machine == '2':
    clear(0)
    stuff = randint(1,10)
    if stuff <= 7:
      if player.gold >= 25:
        player.gold -= 25
        prizes()
      elif player.gold < 25:
        print("As you put the money in the machine you realise that you don't have 25 gold. There is no refund button...")
        wait(4)
        player.gold -= player.gold
        reh()
    elif stuff > 7:
      print("You put in the gold. The machine makes a loud noise and nothing comes out.")
      if player.gold >= 25:
        player.gold -= 25
        wait(3)
        reh()
      else:
        player.gold -= player.gold
        wait(3)
        reh()
  elif machine == '3':
    clear(0)
    print("You punch the machine as hard as possible.")
    clear(2)
    pain = randint(1,10)
    if pain <= 7:
      print("The machine doesn't budge but you break your hand. You lose 64 HP!")
      subtractHealth(64)
      wait(4)
      reh()
    elif pain > 7:
      prizes()
      wait(2)
      reh()
  elif machine == '4':
    clear(0)
    trip = randint(1,10)
    if trip >= 9:
      print("You walk away but trip and lose 4 HP.")
      subtractHealth(4)
      wait(2)
      reh()
    else:
      print("You walked away never to look back again.")
      wait(2)
      reh()
def nothing():
  print("Nothing Happened :)")
  wait(2)
  reh()
def pizza():
  choice = input("""You and you're friend are deciding what kind of pizza to order.
  1. Use Item
  2. Compromise
  3. Battle to the Death
  4. Eat Paper
 """)
  if choice == "1":
    eventStuff.pizza = True
    use()
  elif choice == "2":
    kindness = randint(1,100)
    kindness -= player.childrenKicked * 5
    if kindness < 70:
      clear(1)
      print("You and your friends talk it out. You decide to each pick the toppings on 1/2 of the pizza.")
      wait(1)
      print("All is good.")
      wait(1)
      print("For now...")
      wait(2)
      reh()
    elif kindness > 70:
      clear(1)
      print("Your friend slaps you dealing 53 damage.")
      subtractHealth(53)
      wait(3)
      reh()
  elif choice == "3":
    clear(1)
    print("You both draw your weapons and prepare to duel.")
    clear(1)
    health = randint(1,75)
    combat(health,"Friend",2)
  elif choice == "4":
    clear(1)
    paperPoison = randint(1,10)
    if paperPoison <= 2:
      print("You and your friend eat paper...")
      wait(3)
      print("Turns out it's fly paper...")
      wait(3)
      print("You lose 73 HP...")
      subtractHealth(73)
      wait(3)
      reh()
    elif paperPoison > 2:
      print("You and your friend eat paper...")
      wait(3)
      print("Cool I guess...")
      wait(3)
      if "Paper" in player.inventory:
        reh()
      else:
        player.inventory.append("Paper")
        gear.paperUses = 0
        reh()
def arenas():
  randenemy = randint(0,18)
  enemy = bad.bad_guys[randenemy]
  ename = bad.bad_names[randenemy]
  elevel = bad.bad_level[randenemy]
  print("")
  input("You are fighting a " + ename + ". Press enter to FIGHT!")
  combat(enemy,ename,elevel)
def vehicle():
  car = input("""You are at a car dealership.
  1. Use Item
  2. Test Drive
  3. Walk Away
 """)
  wait(3)
  if car == "1":
    eventStuff.vehicle = True
    use()
  elif car == 2:
    bomb = randint(1,10)
    if bomb < 3:
      print("You're test driving the car.")
      wait(3)
      print("Suddenly it explodes :O")
      wait(3)
      print("Imagine...")
      loser()
    elif bomb >= 3:
      print("You're test driving the car.")
      wait(3)
      print("You like it!")
      wait(1)
      buy = input("""It costs 500 Gold. Do you want to buy it?
      1. Yes
      2. No""")
      if buy == 1 and player.gold >=500:
        player.gold -= 500
        player.carName = input("What car is it?")
      elif buy == 1 and player.gold < 500:
        print("You don't have that money!")
        wait(2)
        print("They kick you out of the dealership.")
        wait(3)
        print("The kick deals 3 damage")
        subtractHealth(3)
        wait(3)
        reh()
      elif buy == "2":
        print("They kick you out for wasting their time.")
        wait(3)
        print("The kick deals 2 damage")
        subtractHealth(2)
        wait(3)
        reh()
  elif car == "3":
    print("You walk away never looking back at the nice cars.")
    wait(3)
    reh()
def shop():
  shopping = input("""You come across a shop in the road.
  1. Use Iem
  2. Enter Shop
  3. Keep Walking
 """)
  if shopping == '1':
    eventStuff.shop = True
    use()
  elif shopping == '2':
    print("You enter the shop and there are some items for sale!")
    one = randint(0,6)
    itemOne = gear.tanames[one]
    onePrice = math.ceil(gear.treasure_armor[one] * 50)
    two = randint(0,6)
    itemTwo = gear.twnames[two]
    twoPrice = math.ceil(gear.treasure_weapon[two] * 50)
      
    buy = input("""
  1. """ + str(itemOne) + " Armor, Price: " + str(onePrice) + """ Gold
  2. """ + str(itemTwo) + "  Price: " + str(twoPrice) + """ Gold
  3. Nice Pumpking 5 Gold""")
    if buy == '1':
      if player.gold >= onePrice:
        player.gold -= onePrice
        player.inventory.append(itemOne)
        print("You bought the item!")
        reh()
      elif player.gold < onePrice:
        print("You can't afford that! Get out!")
        wait(3)
        reh()
    elif buy == '2':
      if player.gold >= twoPrice:
        player.gold -= twoPrice
        player.inventory.append(itemTwo)
        print("You bought the item!")
        reh()
      elif player.gold < twoPrice:
        print("You can't afford that! Get out!")
        wait(3)
        reh()
    elif buy == '3':
      if player.gold >= 5:
        player.gold -= 5
        player.inventory.append("Nice Pumpkin")
        print("You bought the Nice Pumpking!")
        wait(3)
        reh()
      elif player.gold < 5:
        print("You can't afford that! Get out!")
        wait(3)
        reh()
  elif shopping == '3':
    print("You keep on walking...")
    wait(3)
    reh()
  else:
    print("?")
    shop()

def reh():
  player.turns += 1
  clear(0)
  if player.turns == 15:
    win()
  if player.hp <= 0:
    print("You died! Game Over")
  player.gold += player.perTurn
  stats()
  event = randint(1,9)
  if event == 1:
    dog()
  elif event == 2:
    dysentery()
  elif event == 3:
    orphan()
  elif event == 4:
    vending()
  elif event == 5:
    chef()
  elif event == 6:
    nothing()
  elif event == 7:
    arenas()
  elif event == 8:
    pizza()
  elif event == 9:
    vehicle()


reh()