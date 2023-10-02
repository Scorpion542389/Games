import main_menu
import m_Rooms
from random import randint
global characters
characters = ["Mary","Lanny","Scott","Jakob","Mike","Susan","Sophie","Leo"]
global movements
movements = 0
global ai_move
ai_move = 0
global suspects
suspects = 8
global character_turn
character_turn = 0

def set_ups():
  print("""
  PLEASE NOTE THAT THE HIDE OPTION DOES NOTHING ATM
  """)
  murderer = (randint(1,suspects)) - 1
  murder_guy = murderer
  input("You are in a mansion. You are tasked with...")
  movement()
  
def movement():
  global movements
  global character_turn
  global characters
  print("")
  if "You" in m_Rooms.lobby:
    m = input("You are in the lobby with " + str(m_Rooms.lobby) + """. Where would you like to go?
    1. North Hall
    2. West Hall
    3. Court Yard
    4. East Hall""")
    if m == "1":
      m_Rooms.lobby.remove("You")
      m_Rooms.main_north_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    elif m == "2":
      m_Rooms.lobby.remove("You")
      m_Rooms.main_west_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    elif m == "3":
      m_Rooms.lobby.remove("You")
      m_Rooms.courtyard.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    elif m == "4":
      m_Rooms.lobby.remove("You")
      m_Rooms.main_east_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.courtyard:
    m = input("You are in the Courtyard with " + str(m_Rooms.courtyard) + """. Where would you like to go?
    1. Lobby
    2. Outside Path""")
    if m == "1":
      m_Rooms.courtyard.remove("You")
      m_Rooms.lobby.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.courtyard.remove("You")
      m_Rooms.outside_path.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.outside_path:
    m = input("You are in the Outside Path with " + str(m_Rooms.outside_path) + """. Where would you like to go?
    1. Green House
    2. Courtyard""")
    if m == "1":
      m_Rooms.outside_path.remove("You")
      m_Rooms.green_house.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.outside_path.remove("You")
      m_Rooms.courtyard.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.green_house:
    m = input("You are in the Green House with " + str(m_Rooms.green_house) + """. Where would you like to go?
    1. Outside Path""")
    if m == "1":
      m_Rooms.green_house.remove("You")
      m_Rooms.outside_path.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.main_west_hallway:
    m = input("You are in the West Hall with " + str(m_Rooms.main_west_hallway) + """. Where would you like to go?
    1. Garage
    2. Game Room
    3. Lobby
    4. Upstairs""")
    if m == "1":
      m_Rooms.main_west_hallway.remove("You")
      m_Rooms.garage.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.main_west_hallway.remove("You")
      m_Rooms.game_room.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "3":
      m_Rooms.main_west_hallway.remove("You")
      m_Rooms.lobby.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "4":
      m_Rooms.main_west_hallway.remove("You")
      m_Rooms.upstairs.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.game_room:
    m = input("You are in the West Hall with " + str(m_Rooms.main_west_hallway) + """. Where would you like to go?
    1. West Hall""")
    if m == "1":
      m_Rooms.game_room.remove("You")
      m_Rooms.main_west_hall.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.garage:
    m = input("You are in the Garage with " + str(m_Rooms.garage) + """. Where would you like to go?
    1. West Hall
    2. Outside Path""")
    if m == "1":
      m_Rooms.garage.remove("You")
      m_Rooms.main_west_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.garage.remove("You")
      m_Rooms.outside_path.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.main_north_hallway:
    m = input("You are in the North Hall with " + str(m_Rooms.main_north_hallway) + """. Where would you like to go?
    1. Office
    2. Library
    3. Lobby
    4. Basement""")
    if m == "1":
      m_Rooms.main_north_hallway.remove("You")
      m_Rooms.office.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.main_north_hallway.remove("You")
      m_Rooms.library.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "3":
      m_Rooms.main_north_hallway.remove("You")
      m_Rooms.lobby.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "4":
      m_Rooms.main_north_hallway.remove("You")
      m_Rooms.basement.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.office:
    m = input("You are in the Office with " + str(m_Rooms.office) + """. Where would you like to go?
    1. North Hall""")
    if m == "1":
      m_Rooms.office.remove("You")
      m_Rooms.main_north_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.library:
    m = input("You are in the Library with " + str(m_Rooms.library) + """. Where would you like to go?
    1. North Hall""")
    if m == "1":
      m_Rooms.library.remove("You")
      m_Rooms.main_north_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.main_east_hallway:
    m = input("You are in the East Hall with " + str(m_Rooms.main_east_hallway) + """. Where would you like to go?
    1. Dining Room
    2. Kitchen
    3. Lobby""")
    if m == "1":
      m_Rooms.main_east_hallway.remove("You")
      m_Rooms.dining_room.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.main_east_hallway.remove("You")
      m_Rooms.kitchen.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "3":
      m_Rooms.main_east_hallway.remove("You")
      m_Rooms.lobby.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.dining_room:
    m = input("You are in the Dining Room with " + str(m_Rooms.dining_room) + """. Where would you like to go?
    1. East Hall""")
    if m == "1":
      m_Rooms.dining_room.remove("You")
      m_Rooms.main_east_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.kitchen:
    m = input("You are in the Kitchen with " + str(m_Rooms.kitchen) + """. Where would you like to go?
    1. Walk-in Freezer
    2. East Hall""")
    if m == "1":
      m_Rooms.kitchen.remove("You")
      m_Rooms.food_pantry.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.kitchen.remove("You")
      m_Rooms.main_east_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.food_pantry:
    m = input("You are in the Walk-In Freezer with " + str(m_Rooms.food_pantry) + """. Where would you like to go?
    1. Kitchen""")
    if m == "1":
      m_Rooms.food_pantry.remove("You")
      m_Rooms.kitchen.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.basement:
    m = input("You are in the Basement Landing with " + str(m_Rooms.basement) + """. Where would you like to go?
    1. Basement East Hall
    2. Basement South Hall
    3. North Hall""")
    if m == "1":
      m_Rooms.basement.remove("You")
      m_Rooms.basement_east_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.basement.remove("You")
      m_Rooms.basement_south_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "3":
      m_Rooms.basement.remove("You")
      m_Rooms.main_north_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.basement_east_hallway:
    m = input("You are in the Basement East Hall with " + str(m_Rooms.basement_east_hallway) + """. Where would you like to go?
    1. Cellar
    2. Storage Room
    3. Basement Landing""")
    if m == "1":
      m_Rooms.basement_east_hallway.remove("You")
      m_Rooms.cellar.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.basement_east_hallway.remove("You")
      m_Rooms.storage_room.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "3":
      m_Rooms.basement_east_hallway.remove("You")
      m_Rooms.basement.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.basement_south_hallway:
    m = input("You are in the Basement South Hall with " + str(m_Rooms.basement_south_hallway) + """. Where would you like to go?
    1. Basement Landing
    2. Boiler Room""")
    if m == "1":
      m_Rooms.basement_south_hallway.remove("You")
      m_Rooms.basement.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.basement_south_hallway.remove("You")
      m_Rooms.boiler_room.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.boiler_room:
    m = input("You are in the Boiler Room with " + str(m_Rooms.boiler_room) + """. Where would you like to go?
    1. Basement South Hall""")
    if m == "1":
      m_Rooms.boiler_room.remove("You")
      m_Rooms.basement_south_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.storage_room:
    m = input("You are in the Storage Room with " + str(m_Rooms.storage_room) + """. Where would you like to go?
    1. Basement East Hall""")
    if m == "1":
      m_Rooms.storage_room.remove("You")
      m_Rooms.basement_east_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.cellar:
    m = input("You are in the Cellar with " + str(m_Rooms.cellar) + """. Where would you like to go?
    1. Basement East Hall""")
    if m == "1":
      m_Rooms.cellar.remove("You")
      m_Rooms.basement_east_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()  
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.upstairs:
    m = input("You are in the Upstairs Lobby with " + str(m_Rooms.upstairs) + """. Where would you like to go?
    1. West Hall
    2. Upper East Hall
    3. Upper West Hall""")
    if m == "1":
      m_Rooms.upstairs.remove("You")
      m_Rooms.main_west_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()  
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.upstairs.remove("You")
      m_Rooms.top_east_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "3":
      m_Rooms.upstairs.remove("You")
      m_Rooms.top_west_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.master_bedroom:
    m = input("You are in the Master Bedroom with " + str(m_Rooms.master_bedroom) + """. Where would you like to go?
    1. Upper West Hall""")
    if m == "1":
      m_Rooms.master_bedroom.remove("You")
      m_Rooms.top_west_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.kids_room:
    m = input("You are in the Kid's Bedroom with " + str(m_Rooms.kids_room) + """. Where would you like to go?
    1. Upper East Hall
    2. Attic""")
    if m == "1":
      m_Rooms.kids_room.remove("You")
      m_Rooms.top_east_hallway.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.kids_room.remove("You")
      m_Rooms.attic.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(character_turn)
  elif "You" in m_Rooms.attic:
    m = input("You are in the Attic with " + str(m_Rooms.attic) + """. Where would you like to go?
    1. Kid's Bedroom""")
    if m == "1":
      m_Rooms.attic.remove("You")
      m_Rooms.kids_room.append("You")
      if movements < 4:
        movements += 1
        movement()
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.top_east_hallway:
    m = input("You are in the Upper East Hallway with " + str(m_Rooms.top_east_hallway) + """. Where would you like to go?
    1. Upper Lobby
    2. Kid's Bedroom""")
    if m == "1":
      m_Rooms.top_east_hallway.remove("You")
      m_Rooms.upstairs.append("You")
      if movements < 4:
        movements += 1
        movement() 
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.top_east_hallway.remove("You")
      m_Rooms.kids_room.append("You")
      if movements < 4:
        movements += 1
        movement()  
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
  elif "You" in m_Rooms.top_west_hallway:
    m = input("You are in the Upper West Hall with " + str(m_Rooms.top_west_hallway) + """. Where would you like to go?
    1. Upper Lobby
    2. Master Bedroom""")
    if m == "1":
      m_Rooms.top_west_hallway.remove("You")
      m_Rooms.upstairs.append("You")
      if movements < 4:
        movements += 1
        movement()  
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.top_west_hallway.remove("You")
      m_Rooms.master_bedroom.append("You")
      if movements < 4:
        movements += 1
        movement()  
      elif movements >= 4:
        movements = 0
        end_turn(characters[character_turn])

def end_turn(person):
  global ai_move
  global character_turn
  global characters
  global suspects
  print(str(person) + "MOVED!")
  if character_turn == suspects - 1:
    character_turn = 0
    movement()
  print("")
  if person in m_Rooms.lobby:
    m = str(randint(1,4))
    if m == "1":
      m_Rooms.lobby.remove(person)
      m_Rooms.main_north_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    elif m == "2":
      m_Rooms.lobby.remove(person)
      m_Rooms.main_west_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(characters[character_turn])
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    elif m == "3":
      m_Rooms.lobby.remove(person)
      m_Rooms.courtyard.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(characters[character_turn])
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    elif m == "4":
      m_Rooms.lobby.remove(person)
      m_Rooms.main_east_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(characters[character_turn])
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.courtyard:
    m = str(randint(1,2))
    if m == "1":
      m_Rooms.courtyard.remove(person)
      m_Rooms.lobby.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "2":
      m_Rooms.courtyard.remove(person)
      m_Rooms.outside_path.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.outside_path:
    m = str(randint(1,2))
    if m == "1":
      m_Rooms.outside_path.remove(person)
      m_Rooms.green_house.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "2":
      m_Rooms.outside_path.remove(person)
      m_Rooms.courtyard.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.green_house:
    m = str(1)
    if m == "1":
      m_Rooms.green_house.remove(person)
      m_Rooms.outside_path.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.main_west_hallway:
    m = str(randint(1,4))
    if m == "1":
      m_Rooms.main_west_hallway.remove(person)
      m_Rooms.garage.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "2":
      m_Rooms.main_west_hallway.remove(person)
      m_Rooms.game_room.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "3":
      m_Rooms.main_west_hallway.remove(person)
      m_Rooms.lobby.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "4":
      m_Rooms.main_west_hallway.remove(person)
      m_Rooms.upstairs.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.game_room:
    m = str(1)
    if m == "1":
      m_Rooms.game_room.remove("You")
      m_Rooms.main_west_hall.append("You")
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.garage:
    m = str(randint(1,2))
    if m == "1":
      m_Rooms.garage.remove(person)
      m_Rooms.main_west_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "2":
      m_Rooms.garage.remove(person)
      m_Rooms.outside_path.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.main_north_hallway:
    m = str(randint(1,4))
    if m == "1":
      m_Rooms.main_north_hallway.remove(person)
      m_Rooms.office.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "2":
      m_Rooms.main_north_hallway.remove(person)
      m_Rooms.library.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "3":
      m_Rooms.main_north_hallway.remove(person)
      m_Rooms.lobby.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "4":
      m_Rooms.main_north_hallway.remove(person)
      m_Rooms.basement.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.office:
    m = str(1)
    if m == "1":
      m_Rooms.office.remove(person)
      m_Rooms.main_north_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.library:
    m = str(1)
    if m == "1":
      m_Rooms.library.remove(person)
      m_Rooms.main_north_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.main_east_hallway:
    m = str(randint(1,3))
    if m == "1":
      m_Rooms.main_east_hallway.remove(person)
      m_Rooms.dining_room.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "2":
      m_Rooms.main_east_hallway.remove(person)
      m_Rooms.kitchen.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "3":
      m_Rooms.main_east_hallway.remove(person)
      m_Rooms.lobby.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.dining_room:
    m = str(1)
    if m == "1":
      m_Rooms.dining_room.remove("You")
      m_Rooms.main_east_hallway.append("You")
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.kitchen:
    m = str(randint(1,2))
    if m == "1":
      m_Rooms.kitchen.remove(person)
      m_Rooms.food_pantry.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "2":
      m_Rooms.kitchen.remove(person)
      m_Rooms.main_east_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.food_pantry:
    m = str(1)
    if m == "1":
      m_Rooms.food_pantry.remove(person)
      m_Rooms.kitchen.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.basement:
    m = str(randint(1,3))
    if m == "1":
      m_Rooms.basement.remove(person)
      m_Rooms.basement_east_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "2":
      m_Rooms.basement.remove(person)
      m_Rooms.basement_south_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "3":
      m_Rooms.basement.remove(person)
      m_Rooms.main_north_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.basement_east_hallway:
    m = str(randint(1,3))
    if m == "1":
      m_Rooms.basement_east_hallway.remove(person)
      m_Rooms.cellar.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "2":
      m_Rooms.basement_east_hallway.remove(person)
      m_Rooms.storage_room.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
    if m == "3":
      m_Rooms.basement_east_hallway.remove(person)
      m_Rooms.basement.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(character_turn)
  elif person in m_Rooms.boiler_room:
    m = str(1)
    if m == "1":
      m_Rooms.boiler_room.remove(person)
      m_Rooms.basement_south_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn])
  elif person in m_Rooms.storage_room:
    m = str(1)
    if m == "1":
      m_Rooms.storage_room.remove(person)
      m_Rooms.basement_east_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn])
  elif person in m_Rooms.cellar:
    m = str(1)
    if m == "1":
      m_Rooms.cellar.remove(person)
      m_Rooms.basement_east_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn]) 
  elif person in m_Rooms.upstairs:
    m = str(randint(1,3))
    if m == "1":
      m_Rooms.upstairs.remove(person)
      m_Rooms.main_west_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn])  
    if m == "2":
      m_Rooms.upstairs.remove(person)
      m_Rooms.top_east_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn])  
    if m == "3":
      m_Rooms.upstairs.remove(person)
      m_Rooms.top_west_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn])
  elif person in m_Rooms.master_bedroom:
    m = str(1)
    if m == "1":
      m_Rooms.master_bedroom.remove(person)
      m_Rooms.top_west_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn])
  elif person in m_Rooms.kids_room:
    m = str(randint(1,2))
    if m == "1":
      m_Rooms.kids_room.remove(person)
      m_Rooms.top_east_hallway.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.kids_room.remove(person)
      m_Rooms.attic.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn])
  elif person in m_Rooms.attic:
    m = str(1)
    if m == "1":
      m_Rooms.attic.remove(person)
      m_Rooms.kids_room.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn])
  elif person in m_Rooms.top_east_hallway:
    m = str(randint(1,2))
    if m == "1":
      m_Rooms.top_east_hallway.remove(person)
      m_Rooms.upstairs.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn])
    if m == "2":
      m_Rooms.top_east_hallway.remove(person)
      m_Rooms.kids_room.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn])
  elif person in m_Rooms.top_west_hallway:
    m = str(randint(1,2))
    if m == "1":
      m_Rooms.top_west_hallway.remove(person)
      m_Rooms.upstairs.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn]) 
    if m == "2":
      m_Rooms.top_west_hallway.remove(person)
      m_Rooms.master_bedroom.append(person)
      if ai_move < 4:
        ai_move += 1
        end_turn(person)
      elif ai_move >= 4:
        ai_move = 0
        character_turn += 1
        end_turn(characters[character_turn])