import ps
import spells
import bad
import gear
import arena
import og
import mystery
from random import randint
print("You are testing the ALPHA version. Please report any bugs!")
main_menu = "E"

def Main_menu():
  print("")
  main_menu = input("""Choose an option below!!!
  1. Arena
  2. Play the Original Game! (Sepperate from the Arena)""")
  if main_menu == "1":
    ps.hp = 100
    ps.mana = 100
    arena.arenas()
  elif main_menu == "2":
    og.restart()
    og.starting()
  elif main_menu == "3":
    mystery.set_ups()
