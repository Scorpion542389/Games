import main_menu
from random import randint
import ps
# Variables (Default)
global turns
global chance
chance = 0
turns = 0
global inventory
inventory = []
global time
time = 1
global name
name = " "
global paradecandy
paradecandy = 0
global pumpkincandle
pumpkincandle = 0
global dragonfight
dragonfight = 0
global dysentarytf
dysentarytf = 0
global nothing_
nothing_ = 0
global stormtime
stormtime = 0
global gold
gold = 0
global shopping
shopping = 0
global hp
hp = 100
global wooter
wooter = 0
global maxhp
maxhp = 100
global offercount
global brooks
brookz = 0
global goldy
goldy = 0
global bannana
bannana = 0
global goldturns
goldturns = 0
global weathertype
weathertype = " "
global police
police = False
global brooksdead
brooksdead = False
offercount = 0
global newturns
newturns = 0

# Function to start game
def starting():
  global gold
  global bananaeaten
  global maxhp
  global turns
  global dysentarytf
  global name
  global brooksdead
  name = ps.name
  def weather():
    global weathertype
    weathertype = randint(1,5)
    if weathertype == 1:
      weathertype = "Apocolypse"
    elif weathertype == 2:
      weathertype = "Hail"
    elif weathertype == 3:
      weathertype = "Lightning"
    elif weathertype == 4:
      weathertype = "Normal"
    elif weathertype == 5:
      weathertype = "Rain"
    input("You are playing a " + weathertype + " game! (Press Enter to Continue)")
    reh()
  instructions = input("Do you want to know how to play? Y/N")
  instructions = instructions.lower()
  if instructions == "y":
    input("""
    The Goal is to survive for 20 Turns. Press Enter to Continue
    Type 'Inventory' to see your inventory. Press Enter to Continue
    Type "Use" and follow the instructions to use the items in your inventory.
    Type "Stats" to see your HP. If your HP hits 0 then you lose.
    To View how much gold you have look in stats not inventory!
    
    Weather Events:
    - Hail, you take 2 damage at the end of every turn
    - Lightning, there is a 30% chance of a fire starting
    - Apocolypse, 1% of the game ending randomly
    - Normal, Nothing changes
    - Rain, Heal 2 health every turn
    
    Patch Notes:
    - Added the Rock event *Credit Oak Eastland
    - Added way to play again without restarting code
    - Added some QOL updates
    - Bug Fixes
    - Added chance of the police catching you to stats
    
    If any errors occur please DM Scorpion54#2389 on Discord.
    """ )
  prolouge = input("""
  Are you ready? Y/N""")
  prolouge = prolouge.lower()
  if name == "Brooks":
    dysentarytf = 1
  prolouge = prolouge.lower()
  if prolouge == "dev":
    shop()
  elif prolouge == "y":
    print("Here we go")
    weather()
  elif prolouge == "n":
    print("""
    Too Bad""")
    weather()
  else:
    print("ERROR")

# HP System
def addhealth(amountadd):
  global hp
  global turns
  global maxhp
  hp = hp + amountadd
  if hp > maxhp:
    leftover = hp - 100
    toomuch = amountadd - leftover
    hp = 100
    print(toomuch, "HP was added to your health")
    print("HP:", hp)
    reh()
  print(amountadd, "HP was added to your health")
  print("HP:", hp )
  reh()
def subtracthealth(amountsubtract):
  global hp
  global turns
  hp = hp - amountsubtract
  print("HP:", hp)
  if hp <= 0:
    print("You Died")
    gameend()
  else:
    turnupdate()
    if turns == 20:
      gameend()
    elif turns < 20:
      reh()
    elif turns > 20:
      return
    else:
      print("HP:", hp)
      turnupdate()
      input("Press Enter to Continue")
      reh()

# Important Stuff
def restart():
  global turns
  global chance
  global newturns
  newturns = 0
  chance = 0
  turns = 0
  global inventory
  inventory = []
  global time
  time = 1
  global paradecandy
  paradecandy = 0
  global pumpkincandle
  pumpkincandle = 0
  global dragonfight
  dragonfight = 0
  global dysentarytf
  dysentarytf = 0
  global nothing_
  nothing_ = 0
  global stormtime
  stormtime = 0
  global gold
  gold = 0
  global shopping
  shopping = 0
  #Health System
  global hp
  hp = 100
  global wooter
  wooter = 0
  global maxhp
  maxhp = 100
  global offercount
  global brooks
  brookz = 0
  global goldy
  goldy = 0
  global bannana
  bannana = 0
  global goldturns
  goldturns = 0
  global weathertype
  weathertype = " "
  global police
  police = False
  global brooksdead
  brooksdead = False
  offercount = 0
  starting()
def gameend():
  global name
  end = input("The game is over. Would you like to play again " + name + "?")
  main_menu.Main_menu()
def use():
  global inventory
  global pumpkincandle
  global paradecandy
  global dragonfight
  global turns
  global nothing_
  global stormtime
  global shopping
  global wooter
  global goldy
  global brookz
  global brooksdead
  item = input("Type the Name of the Item You want to use")
  if item == "a nice pumpkin" and item in inventory:
      print("You used the nice pumpkin")
      inventory.remove("A Nice Pumpkin")
      pumpkin = 0
  if item == "Parade Candy" and item in inventory:
    print("You ate the candy. You healed all your health!!!")
    addhealth(500)
    inventory.remove("Parade Candy")
    candy = 0
  if item == "Yellow Banana" and item in inventory:
    topbottom = input("Do you peel it from the top or bottom? Top/Bottom")
    topbottom = topbottom.lower()
    inventory.remove("Yellow Banana")
    dysentarytf = 1
    bannana = 0
    if topbottom == "top":
      for _ in range(1):
        deatht = randint(1, 10)
        if deatht <= 2:
          print("The Banana ate you before you could eat it")
          print("The End")
          print("Restart code to play again!")
          gameend()
        elif deatht > 2:
          print("You ate the banana and felt healthier (you can't get sick for the rest of this game) and you healed 10 HP")
          addhealth(10)
          dysentartf = 1
          input("Press Enter to Continue")
    if topbottom == "bottom":
      for _ in range(1):
        deathb = randint(1, 100)
      if deathb <= 5:
        input("You peel it from the bottom and the game has decided you shall win!!!")
        turns = 20
        turnupdate()
      elif deathb > 5:
        print("You peel it from the bottom. You monster. The game decides its your time to die.")
        print("""
        The End""")
        gameend()
        return
  elif item == "a bad pumpkin" and item in inventory:
    print("Nope")
    reh()
  elif item == "Coconut" and item in inventory:
    if brookz == 1 and brooksdead == False:
      input("You killed Brooks for the rest of the game. Because he doesn't like coconuts. (Press Enter to Continue)")
      brooksdead = True
      inventory.remove("Coconut")
      turnupdate()
      reh()
      return
    else:
      input("You can't use that here")
  else:
    if pumpkincandle == 1:
      pumpkincandle = 0
      candle_pumpkin()
    elif paradecandy == 1:
      paradecandy = 0
      parade()
    elif dragonfight == 1:
      dragonfight = 0
      dragon()
    elif nothing_ == 1:
      nothing_ = 0
      nothing()
    elif stormtime == 1:
      stormtime = 0
      storm()
    elif shopping == 1:
      shopping = 0
      shop()
    elif wooter == 1:
      wooter = 0
      magicwater()
    elif goldy == 1:
      goldy = 0
      goldland()
    elif brookz == 1:
      brookz = 0
      brooks()
    else:
      print("ERROR")
  if pumpkincandle == 1:
    pumpkincandle = 0
    candle_pumpkin()
  elif paradecandy == 1:
    paradecandy = 0
    parade()
  elif dragonfight == 1:
    dragonfight = 0
    dragon()
  elif nothing_ == 1:
    nothing_ = 0
    nothing()
  elif stormtime == 1:
    stormtime = 0
    storm()
  elif shopping == 1:
    shopping = 0
    shop()
  elif wooter == 1:
    wooter = 0
    magicwater()
  elif brookz == 1:
    brookz = 0
    brooks()
  elif goldy == 1:
    goldy = 0
    goldland()
  else:
    print("ERROR")
def wait():
  global turns
  global time
  for _ in range(1):
      wait_ = randint(1, 10)
  if time == 10:
    if turns == 20:
      gameend()
    elif turns < 20:
      print("You waited so long that you died of old age")
      print("The End")
      print("Restart code to play again!")
      gameend()
  elif wait_ <= 2:
    print("The Parade Passes By")
    turnupdate()
    input("Press Enter to Continue")
    time = 1
    reh()
  elif wait_ > 2:
    print("The Parade just keeps going")
    print(time)
    input("Press Enter to keep waiting")
    time = time + 1
    wait()
def stat():
  global pumpkin
  global pumpkincandle
  global paradecandy
  global dragonfight
  global candy
  global bannana
  global dysentarytf
  global turns
  global stormtime
  global gold
  global shopping
  global name
  global turns
  global wooter
  global nothing_
  global goldy
  global brookz
  global chance
  print("""
  """)
  print("Stats:")
  print(name)
  print("HP:" + str(hp))
  print("GOLD COINS:" + str(gold))
  print("Turns Completed:" + str(turns))
  print("Chance of being caught by police: " + str(chance) + "%")
  input("""
  Press Enter to go Back.""")
  if pumpkincandle == 1:
    pumpkincandle = 0
    candle_pumpkin()
  elif paradecandy == 1:
    paradecandy = 0
    parade()
  elif dragonfight == 1:
    dragonfight = 0
    dragon()
  elif stormtime == 1:
    stormtime = 0
    storm()
  elif shopping == 1:
    shopping = 0
    shop()
  elif wooter == 1:
    wooter = 0
    magicwater()
  elif nothing_ == 1:
    nothing_ == 0
    nothing()
  elif brookz == 1:
    brookz = 0
    brooks()
  elif goldy == 1:
    goldy = 0
    goldland()
  else:
    print("ERROR")
def addpumpkin():
  inventory.append("A Nice Pumpkin")
  pumpkin = 1

# Turn Counter
def turnupdate():
  global turns
  global name
  global newturns
  turns = turns + 1
  if newturns > 0:
    if turns == 20:
      print(name + " WON!!! Restart code to play again!!!")
      gameend()
    else:
      newturns += 1
      turnstotal = """
      {} Turns Complete""".format(newturns)
      print(turnstotal)
  else:
    if turns == 20:
      print(name + " WON!!! Restart code to play again!!!")
      gameend()
    else:
      turnstotal = """
      {} Turns Complete""".format(turns)
      print(turnstotal)

# Events
def dragon():
  global turns
  global dragonfight
  choiced = input("A dragon apears do you Fight it or Hide?")
  choiced = choiced.lower()
  if choiced == "inventory":
    print(inventory)
    dragon()
  elif choiced == "use":
    dragonfight = 1
    use()
  elif choiced == "stats":
    dragonfight = 1
    stat()
  elif choiced == "fight":
    for _ in range(1):
      choicef = randint(1, 10)
    if choicef <= 6:
      print("You defeated the dragon!!!")
      turnupdate()
      if turns == 20:
        return
      elif turns < 20:
        reh()
      elif turns > 20:
        return
      input("Press Enter to Continue")
      reh()
    elif choicef > 6:
      print("You fight the dragon but it wins. You lose 50 HP")
      subtracthealth(50)
      if turns == 20:
        return
      elif turns < 20:
        reh()
      elif turns > 20:
        return
  elif choiced == "hide":
    for _ in range(1):
      choiceh = randint(1, 10)
    if choiceh <= 4:
      print("The Dragon got bored and flew away!!!")
      turnupdate()
      input("Press Enter to Continue")
      reh()
    elif choiceh > 4:
      print("The dragon found you and killed you!")
      gameend()
      print("Restart code to play again!")
  elif choiced == "Dev":
    shop()
  else:
    print("Try again :D")
    dragon()
def dysentary():
  global dysentarytf
  global inventory
  global gold
  survive = randint(1,2)
  if dysentarytf == 0:
    if survive == 1:
      print("You got Dysentary... You Died")
      print("The End")
      print("Restart code to play again!")
      gameend()
    elif survive == 2:
      input("You survived dyesntary but lost all of you items and gold to pay the medical bills.")
      inventory == []
      gold = 0
      turnupdate()
      reh()
  elif dysentarytf == 1:
    print("No Sickness")
    reh()
def candle_pumpkin():
  global inventory
  global pumpkin
  global pumpkincandle
  candle = input("You just carved a pumpkin. Do you put a candle in it? Y/N")
  candle = candle.lower()
  if candle == "inventory":
    print(inventory)
    candle_pumpkin()
  elif candle == "use":
    pumpkincandle = 1
    use()
  elif candle == "stats":
    pumpkincandle = 1
    stat()
  elif candle == "y":
    for _ in range(1):
      candlec = randint(1, 2)
    if candlec == 1:
      if "A Nice Pumpkin" in inventory:
        print("You look at your pumpkin and cry because you already have a pumpkin.")
        turnupdate()
        input("Press Enter to Continue")
        reh()
      else:
        print("You have a nice pumpkin now (A nice pumpkin was put into your inventory)")
        turnupdate()
        addpumpkin()
        input("Press Enter to Continue")
        turnupdate()
        if turns == 20:
          return
        elif turns < 20:
          reh()
        elif turns > 20:
          return
    if candlec == 2:
      print("You put the candle in the pumpkin and the pumpkin starts to stand up. It attacks you. You lose 10 HP")
      subtracthealth(10)
  if candle == "n":
    for _ in range(1):
      candlen = randint(1, 10)
    if candlen <= 6:
      print("You just leave the pumpkin there to rot")
      input("Press Enter to Continue")
      turnupdate()
      reh()
    elif candlen > 6:
      print("The Pumpkin gets mad at you and attacks you with a knife. You lose 75 HP")
      subtracthealth(75)
  else:
    print("Try again :D")
    candle_pumpkin()
  if turns == 20:
    return
  elif turns < 20:
    reh()
  elif turns > 20:
    return
def nothing():
  next = input("""Nothing Happened :D
  """)
  if next == "Inventory":
    print(inventory)
  elif next == "Stats":
    stat()
  elif next == "Use":
    nothing = 1
    use()
  else:
    turnupdate()
    reh()
def parade():
  global turns
  global paradecandy
  paradec = input("A parade has crossed paths with you. Do you wait or run throug? Run/Wait")
  paradec = paradec.lower()
  if paradec == "inventory":
    print("""INVENTORY
    """)
    print(inventory)
    parade()
  elif paradec == "use":
    paradecandy = 1
    use()
  elif paradec == "stats":
    paradecandy = 1
    stat()
  elif paradec == "wait":
    for _ in range(1):
      waitl = randint(1, 10)
    if waitl <=2:
      print("The parade leaves immidiatly")
      turnupdate()
      if turns == 20:
          return
      elif turns < 20:
        input("Press Enter to Continue")
        reh()
      elif turns > 20:
        return
    elif waitl > 2:
      input("The parade keeps going (While you wait turns don't count). Press Enter to Continue")
      wait()
  elif paradec == "run":
    for _ in range(1):
      run = randint(1, 10)
    if run <= 7:
      print("You got trampled for an hour. You lose 99 HP")
      input("Press Enter to Continue")
      subtracthealth(99)
    elif run > 7:
      candy = input("While running thorugh the parade you see a peice of candy. Do you Pick it up? Y/N")
      candy = candy.lower()
      if candy == "y":
        if "Parade Candy" in inventory:
          print("You decide 1 peice of candy is enough and leave it on the ground")
        else:
          inventory.append("Parade Candy")
          candy = 1
          print("You Pick up the candy and walk throught the parade")
        input("Press enter to continue")
        turnupdate()
        reh()
      elif candy == "n":
        print("You decide not to take the delicous treat.")
        input("Press Enter to continue")
        if turns == 20:
          return
        elif turns < 20:
          reh()
        elif turns > 20:
          return
    else:
      print("ERROR")
  else:
    print("Try Again :D")
    parade() 
def bannanatime():
  global bannana
  look = input("You are in a forest and you are hungry. Do you look for a banana in the tree or bush? Tree/Bush")
  look = look.lower()
  if look == "inventory":
    print(inventory)
    bannanatime()
  elif look == "use":
    bannana = 1
    use()
  elif look == "stats":
    bannana = 1
    stat()
  elif look == "bush":
    for _ in range(1):
      bushlook = randint(1, 10)
    if bushlook <= 3:
      if bannana == 0:
        print("You found a banana on the floor. (It was put into your inventory)")
        inventory.append("Yellow Banana")
        bannana = 1
        turnupdate()
        input("Press Enter to Continue")
        if turns == 20:
          return
        elif turns < 20:
          reh()
        elif turns > 20:
          return
      elif bannana == 1:
        print(" You found another banana. You decide to leave it there since you already have one")
        turnupdate()
        input("Press Enter to Continue")
        reh()
    elif bushlook > 3:
      print("You look in the bush to find... nothing")
      input("The bush cut you with it's thorns too... (Press Enter to Continue)")
      input("You lost 1 HP... (Press Enter to Continue)")
      subtracthealth(1)
  if look == "tree":
    for _ in range(1):
      treelook = randint(1, 10)
    if treelook >= 8:
      print("You climb a tree to find a banana")
      print("You find a coconut. But instead of putting it in your inventory you throw it away")
      input("Because coconuts are bad. (Press Enter to Continue)")
      input("You lose 1 HP for touching a coconut (Press Enter to Continue)")
      subtracthealth(1)
    elif treelook < 8:
      print("You climb the tree to find a banana")
      print("When you reach the top there is a monkey with a Banana.")
      monkey = input("Do you take the banana or climb back down? Take/Climb")
      monkey = monkey.lower()
      if monkey == "take":
        print("The monkey is offended and hits you with a coconut.")
        print("Because its a coconut you lose 89 HP.")
        subtracthealth(89)
      elif monkey == "climb":
        for _ in range(1):
          climbluck = randint(1, 10)
        if climbluck >= 4:
          print("You climb to the ground but accidentally cut yourself on a coconut.")
          print("You lose 2 HP")
          subtracthealth(2)
        elif climbluck < 4:
          print("You slip and fall about 20 Feet.")
          print("You lose 12 HP")
          subtracthealth(12)
  else:
    print("Try Again :D")
    bannanatime()
def storm():
  global gold
  global stormtime
  stormc = input("You are traveling on a road and a storm comes. Do you hide in a nearby cave or keep walking? Cave/Walk")
  stormc = stormc.lower()
  if stormc == "inventory":
    print("""INVENTORY
    """)
    print(inventory)
    storm()
  elif stormc == "use":
    stormtime = 1
    use()
  elif stormc == "stats":
    stormtime = 1
    stat()
  elif stormc == "cave":
    for _ in range(1):
      cavehide = randint(1, 10)
    if cavehide < 3:
      input("You feel somthing in the cave. (Press Enter to Continue)")
      input("It's a bear... (Press Enter to Continue)")
      input("You lose 50 HP... (Press Enter to Continue)")
      subtracthealth(50)
    elif cavehide == 9:
      input("You found a gold coin. A sense that you can use this at a shop. (Press Enter to Continue)")
      gold = gold + 1
      turnupdate()
      reh()
    elif cavehide >= 3:
      print("The Storm Passes By but there were coconuts in the cave")
      input("Press Enter to Continue")
      input("You lose 5 HP for being near coconuts (Press Enter to Continue)")
      subtracthealth(5)
  elif stormc == "walk":
    for _ in range(1):
      stormwalk = randint(1, 10)
    if stormwalk >= 3:
      print("You get struck by lightning")
      input("Press Enter to Continue")
      input("You lose 99.99 HP (Press Enter to Continue")
      subtracthealth(99.99)
    elif stormwalk < 3:
      goldpick = input("You find alot of shiny peices in the road. Do you pick them up? Y/N")
      goldpick = goldpick.lower()
      if goldpick == "y":
        print("You pick up 500 gold coins. You wonder if you can use them at the new shop.")
        gold = gold + 500
        input("Press Enter to Continue")
        reh()
      elif goldpick == "n":
        print("You decide not to pick up the useless gold.")
        input("Press Enter to Continue")
        reh()
  else:
    print("Try Again :D")
    storm()
def shop():
  global gold
  global candy
  global badpumpkin
  global police
  global inventory
  global chance
  global shopping
  shopc = input("You Find a shop on the road. Do you shop or keep walking? Shop/Walk or...")
  shopc = shopc.lower()
  if shopc == "inventory":
    print(inventory)
    shop()
  elif shopc == "use":
    shopping = 1
    use()
  elif shopc == "stats":
    shopping = 1
    stat()
  elif shopc == "shop":
    print("Items")
    print("""
    1. Parade Candy - 500 Gold""")
    print("""
    2. A Bad Pumpkin - 30 Gold""")
    print("""
    3. Bear Spray - 100000 Gold""")
    print("""
    4. Coconut - 5000 Gold)""")
    print("""(Type "Back" to leave the store)""")
    shopitem = input("What would you like to buy? 1/2/3/4")
    if shopitem == "1":
      if gold >= 50:
        gold = gold - 50
        inventory.append("Parade Candy")
        print("You Bought the Parade Candy")
        input("Now leave. (Press Enter to Continue)")
        turnupdate()
        reh()
      elif gold < 50:
        print("You don't have enough gold lol.")
        input("Now leave. (Press Enter to Continue)")
        turnupdate()
        reh()
    elif shopitem == "2":
      if gold >= 30:
        gold = gold - 30
        inventory.append("A Bad Pumpkin")
        print("You bought the Bad Pumpkin.... shame")
        input("Now leave. (Press Enter to Continue)")
        turnupdate()
        reh()
      elif gold < 30:
        print("You don't have enough gold lol.")
        input("Now leave. (Press Enter to Continue)")
        turnupdate()
        reh()
    elif shopitem == "3":
      if gold >= 100000:
        print("I actaully have sentimental value to this.... Sorry")
        input("Now leave. (Press Enter to Continue)")
        turnupdate()
        reh()
      elif gold < 100000:
        print("No lol")
        input("Press Enter to Continue")
        turnupdate()
        reh()
    elif shopitem == "4":
      if gold >= 5000:
        gold = gold - 5000
        inventory.append("Coconut")
        print("You bought the coconut. You monster.")
        input("Now leave. (Press Enter to continue.")
        turnupdate()
        reh()
      elif gold < 5000:
        print("You don't have enough gold lol.")
        input("Now leave. (Press Enter to Continue)")
        turnupdate()
        reh()
    elif shopitem == "back" or "Back":
      input("You left the shop.")
      turnupdate()
      reh()
  elif shopc == "walk":
    input("Press Enter to Continue")
    turnupdate()
    reh()
  elif shopc == "":
    e = input("Or... Rob")
    e = e.lower()
    if e == "rob":
      randgold = randint(1,1000000)
      gold = gold + randgold
      randitem = randint(1,3)
      if randitem == 1:
        inventory.append("Yellow Banana")
        randitem = "Yellow Banana"
      if randitem == 2:
        inventory.append("Parade Candy")
        randitem = "Parade Candy"
      if randitem == 3:
        inventory.append("Coconut")
        randitem = "Coconut"
      if police == True:
        input("The police become more alert!")
        chance = chance + 10
      else:
        input("You rob the store and you get " + str(randgold) + " you get a " + str(randitem))
        input("The police are after you now. You can't go to the shop because you will get caught.")
        police = True
        turnupdate()
        reh()
    else:
      print("I don't understand. Try again!")
      shop()
  else:
    print("Try again")
    shop()
def magicwater():
  global gold
  global bananaeaten
  global inventory
  global dysentarytf
  global wooter
  waterfc = input("You come across a lake. Do you swim in it or take a drink? Swim/Drink")
  waterfc = waterfc.lower()
  if waterfc == "inventory":
    print(inventory)
    magicwater()
  elif waterfc == "use":
    wooter = 1
    use()
  elif waterfc == "stats":
    wooter = 1
    stat()
  elif waterfc == "swim":
    for _ in range(1):
      monster = randint(1, 10)
      if monster <= 9:
        seadragon = input("A Sea Dragon appears. Do you Fight it or Swim away? Fight/Swim")
        seadragon = seadragon.lower()
        if seadragon == "fight":
          for _ in range(1):
            win = randint(1, 10)
          if win <= 7:
            input("You defeated the seadragon! (Press Enter to Continue)")
            turnupdate()
            reh()
          elif win > 7:
            input("The Sea Dragon beat you up. You lost 37 Health (Press Enter to Continue)")
            subtracthealth(37)
        elif seadragon == "swim":
          for _ in range(1):
            swimming = randint(1, 10)
          if swimming <= 6:
            input("You swam and hid in some tall grass. The dragon didn't find you because Seadragon's have bad eyesight. (Press Enter to Continue)")
            turnupdate()
            reh()
          elif swimming > 6:
            input("You try to swim away but the Sea Dragon hears you because your a loud swimmer. You lose 28 health.")
            subtracthealth(28)
      elif monster > 9:
        input("The swim was refreshing. You regained all your health. (Press Enter to Continue)")
        addhealth(1000)
        reh()
  elif waterfc == "drink":
    for _ in range(1):
      water = randint(1, 3)
    if water == 3:
      input("You lose 63 health but magically gain 2,000 gold. (Press Enter to Continue)")
      gold = gold + 2000
      subtracthealth(63)
    elif water == 2:
      input("You lose 38 health but you can't get sick anymore (Press Enter to Continue)")
      dysentarytf = 1
      subtracthealth(38)
    elif water == 1:
      input("You are fully healed but, you lose all you gold and items.")
      gold = gold - gold
      inventory = []
      turnupdate()
      addhealth(100)
  else:
    print("Try Again")
    magicwater()
def brooks():
  global gold
  global inventory
  global offercount
  global brookz
  a = input("A Brooks the albino silver back gorilla appears. He is holding a rather large club. He requests a banana and 100 gold from you. (You can type use or stats now. If you don't want to just press enter)")
  a = a.lower()
  if a == "inventory":
    print(inventory)
    brooks()
  elif a == "use":
    brookz = 1
    use()
  elif a == "stats":
    brookz = 1
    stat()
  if gold >= 5 and "Yellow Banana" in inventory:
    def haveit():
      global gold
      havec = input("Do you give it to him or try to trick him? Give/Trick")
      havec = havec.lower()
      if havec == "give":
        gold -= 5
        inventory.remove("Yellow Banana")
        input("You gave brooks the banana and gold. He lets you pass. (Press Enter to Continue)")
        turnupdate()
        reh()
      elif havec == "trick":
        for _ in range(1):
          trickc = randint(1, 11)
        if trickc <= 5:
          input("You tell brooks that you will get him a banana later. He believes your lie (Press Enter to continue)")
          reh()
        elif trickc > 5:
          input("You tell him that your banana has gone bad but he doesnt believe you. He hits you with his club for 75 damage! (Press Enter to Continue)")
          subtracthealth(75)
      else:
        print("Try Again")
        haveit()
    haveit()
  else:
    def donthave():
      global offercount
      donth = input("You don't have the stuff he wants. Do you want to run away or bargain with brooks? Run/Bargain")
      donth = donth.lower()
      if donth == "run":
        for _ in range(1):
          running = randint(1, 10)
        if running >= 3:
          input("Brooks big club is to long for you to run from and he hits you dealing 27 damage. (Press Enter to Continue)")
          subtracthealth(27)
        elif running < 3:
          input("You were able to escape from Brooks... for now. (Press Enter to Continue)")
          turnupdate()
          reh()
      elif donth == "bargain":
          print("Brooks will accept a random amount of gold between 1 and 1000 gold. You have 3 offers for brooks. (You must guess Brook's number or above then pay that much gold)")
          def guessing():
            global gold
            global offercount
            for _ in range(1):
              newgold = randint(1, 1000)
            guess = input("Offer:")
            if int(guess) >= newgold:
              if gold >= int(guess):
                input("He accepts your deal and lets you go. (Press Enter to Continue)")
                gold -= int(guess)
                turnupdate()
                reh()
              else:
                input("You don't have that much gold. He takes all your gold and deals 57 damage while taking your gold. (Press Enter to Continue)")
                gold -= gold
                subtracthealth(57)
            elif int(guess) < newgold:
              if offercount <= 3:
                print("Try again!")
                offercount += 1
                donthave()
              else:
                input("Brooks gets tired of your offers and hits you dealing 15 damage")
                subtracthealth(15)
          guessing()
      else:
        donthave()
    offercount = 0
    donthave()
def goldz():
  global inventory
  global gold
  global goldturns
  global hp
  goldturns = 0
  if "A Nice Pumpkin" in inventory:
    input("""
    You fall into the well but, the Nice Pumpkin sacraficed itself to break your fall. (Press Enter to Continue)""")
    input("""
    You seem to be in a yellow gold land. You must search for a new well to escape! (Turns dont count in the gold demension! Press Enter to Continue)""")
    input("""
    Psst you pick up 10 gold every turn in the gold demension. Maybe some new stuff will come to find too! (Press Enter to actually Continue)""")
    def look():  
      global gold
      global goldturns
      escape = randint(1,100)
      if escape == 1:
        gold += 10
        input("You found a new well! (Press Enter to Continue)")
        reh()
      elif escape > 1:
        if goldturns == 5:
          firstnumber = randint(1,100)
          secondnumber = randint(1,100)
          thirdnumber = randint(1,10)
          awnser = firstnumber + secondnumber + thirdnumber
          userawnser = int(input("What is " + str(firstnumber) + "+" + str(secondnumber) + "+" + str(thirdnumber)))
          if userawnser == awnser:
            input("Good Job! Keep Going (Press Enter to Continue")
            goldturns = 0
            look()
          else:
            input("WRONG!!! You lose half your gold!")
            gold = gold / 2
            goldturns = 0
            look()
        else:
          gold += 10
          goldturns += 1
          input("Nothing :) (Press Enter to Continue)")
          look()
    look()
  else:
    def look():  
      global gold
      global goldturns
      escape = randint(1,100)
      if escape == 1:
        gold += 10
        input("You found a new well! (Press Enter to Continue)")
        reh()
      elif escape > 1:
        if goldturns == 5:
          firstnumber = randint(1,100)
          secondnumber = randint(1,100)
          thirdnumber = randint(1,10)
          awnser = firstnumber + secondnumber + thirdnumber
          userawnser = int(input("What is " + str(firstnumber) + "+" + str(secondnumber) + "+" + str(thirdnumber)))
          if userawnser == awnser:
            input("Good Job! Keep Going (Press Enter to Continue")
            goldturns = 0
            look()
          else:
            input("WRONG!!! You lose half your gold!")
            gold = gold / 2
            goldturns = 0
            look()
        else:
          gold += 10
          goldturns += 1
          input("Nothing :) (Press Enter to Continue)")
          look()
    input("You fell into the well and break your legs. You lose 99.999999 health. (Press Enter to Continue)")
    hp -= 99.999999
    input("""
    You seem to be in a yellow gold land. You must search for a new well to escape! (Turns dont count in the gold demension! Press Enter to Continue)""")
    input("""
    Psst you pick up 10 gold every turn in the gold demension. Maybe some new stuff will come to find too! (Press Enter to actually Continue)""")
    look()
def goldland():
  global gold
  global hp
  global maxhp
  global inventory
  global goldy
  goldness = input("You come across a well do you make a wish or walk away? Wish/Walk")
  goldness = goldness.lower()
  if goldness == "inventory":
    print(inventory)
    goldland()
  elif goldness == "stats":
    goldy = 1
    stat()
  elif goldness == "use":
    goldy = 1
    use()
  if goldness == "walk":
    for _ in range(1):
      choicew = randint(1, 10)
    if choicew <= 2:
      input("You trip and fall into the well. (Press Enter to Continue)")
      goldz()
    elif choicew > 2:
      input("You keep walking as you wonder about the future. (Press Enter to Continue)")
      turnupdate()
      reh()
    else:
      print("ERROR")
  elif goldness == "wish":
    def wishingness():  
      global maxhp
      global hp
      global inventory
      global pumpkin
      global gold
      wishing = input("What do you wish for? Money/Health/Pumpkin")
      wishing = wishing.lower()
      if wishing == "pumpkin":
        input("You wished for a pumpking a got one.")
        for _ in range(1):
          pumpkining = randint(1, 2)
        if pumpkining == 1:
          inventory.append("A bad pumpking")
          turnupdate()
          reh()
        elif pumpkining == 2:
          inventory.append("A Nice Pumpkin")
          pumpkin = 1
          turnupdate()
          reh()
        else:
          print("ERROR")
      elif wishing == "money":
        adding = randint(1,10000)
        gold = gold + adding
        input("You got " + str(adding) + " more gold! (Press Enter to Continue)")
        turnupdate()
        reh()
      elif wishing == "health":
        yn = randint(1,2)
        if yn == 1:
          hp = maxhp
          input("Your health is maxed out! (Press enter to Continue)")
          turnupdate()
          reh()
        else:
          input("You have gained one health to your max health (Press Enter to Continue)")
          maxhp += 1
          turnupdate()
          reh()
      else:
        print("Try again")
        wishingness()
    wishingness()
  else:
    print("Try Again")
    goldland()
def rock():
  global turns
  rockc = input("You find a rock on the side of the road. Pick Up/Stare")
  rockc = rockc.lower()
  if rockc == "pick up":
    magics = randint(1,10)
    if magics <= 3:
      input("The rock yells at you to put it down. It is the fabled magic rock!")
      wish = input("The fabled magic rock offers you a wish. What do you wish for?")
      wish = wish.lower()
      if "win" in wish:
        print("Ok you win!")
        gameend()
      else:
        input("That is a stupid wish. Go away")
        turnupdate()
        reh()
    elif magics > 3:
      input("You bend over to grab the rock but it turns out it is someones bald head! (Press Enter to Continue)")
      input("The shiny head blinds you, dealing 13 damage.")
      subtracthealth(13)
    else:
      print("ERROR")
  elif rockc == "stare":
    global newturns
    input("You stare at the rock for so long you lose track of your turns. (Press Enter to Continue)")
    newturns = randint(1,20)
    input("You figure you are on turn " + str(newturns) + " (Press Enter to Continue)")
    reh()

# Random Event Handler (REH)
def reh():
  global dysentarytf
  global weathertype
  global hp
  global brooksdead
  global police
  global inventory
  if weathertype == "Hail":
    hp -= 2
    print("The hail is hitting you")
  elif weathertype == "Normal":
    pass
  elif weathertype == "Apocolypse":
    theend = randint(1,100)
    if theend == 1:
      input("The world has ended from the apocolypse! (Press Enter to Die)")
      gameend()
  elif weathertype == "Lightning":
    fireturns = 0
    def fires():
      fire = randint(1,100)
      if fire < 30:
          input("The fire went out! (Press Enter to Continue)")
          reh()
      elif fire >= 30:
          if fireturns == 5:
            firstnumber = randint(1,100)
            secondnumber = randint(1,100)
            thirdnumber = randint(1,10)
            awnser = firstnumber + secondnumber + thirdnumber
            userawnser = int(input("What is " + str(firstnumber) + "+" + str(secondnumber) + "+" + str(thirdnumber)))
            if userawnser == awnser:
              input("Good Job! Keep Going (Press Enter to Continue")
              fireturns = 0
              fires()
            else:
              input("WRONG!!! You lose half your gold!")
              gold = gold / 2
              fireturns = 0
              fires()
          else:
            fireturns += 1
            input("Nothing :) (Press Enter to Continue)")
            fires()
  elif weathertype == "Rain":
    print("The rain heals you 2 hp")
    hp += 2
  else:
    print("ERROR")
  if "Coconut" in inventory:
    print("You lose 0.5 hp for having a coconut in your inventory")
    hp -= 0.5
  if police == True:
    global chance
    caught = randint(1,100)
    if caught <= chance:
      input("The police catch you and you are sentenced to life in jail.")
      gameend()
    elif caught > chance:
      chance += 3
      print("Your chance of being caught by the police has gone up!")
  print("""
  """)
  for _ in range(1):
    randevent = randint(1, 12)
  if turns == 20:
    gameend()
  elif turns > 20:
    gameend()
  else:
    if randevent == 1:
      dragon()
    elif randevent == 2:
      nothing()
    elif randevent == 3:
      if dysentarytf == 1:
        reh()
      elif dysentarytf == 0:
        dysentary()
      else:
        print("ERROR")
    elif randevent == 4:
      candle_pumpkin()
    elif randevent == 5:
      parade()
    elif randevent == 6:
      bannanatime()
    elif randevent == 7:
      storm()
    elif randevent == 8:
      shop()
    elif randevent == 9:
      magicwater()
    elif randevent == 10:
      if brooksdead == True:
        input("You walk by Brooks' dead body.")
        turnupdate()
        reh()
      elif brooksdead == False:  
        brooks()
      else:
        print("ERROR")
    elif randevent == 11:
      goldland()
    elif randevent == 12:
      rock()
    else:
      print("ERROR")