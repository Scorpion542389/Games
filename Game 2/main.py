from random import randint
import ps
import gear
import bad
import arena
inp = ps.inputs
from turtle import *
import main_menu
tommy = Turtle()
def stats():
  print("Age: " + str(ps.age) + 
  " HP: " + str(ps.hp) +
  " Money: " + str(ps.money)
  + " Level: " + str(ps.level) +
  " Magic: " + str(ps.magic) +
  " Charisma: " + str(ps.charisma) + 
  " Strength: " + str(ps.strength) +
  " Inventory: " + str(ps.inventory))
  inp = "done"  

def home_screen():
  tommy.write("Game against humanity ALPHA", None, "center", "23pt bold")
  tommy.penup()
  tommy.goto(0,-50)
  tommy.write("The game against you and coconuts", None, "center", "16pt bold")
  tommy.goto(0,-100)
  tommy.write("Psst the game is  below. You can drag it above the logo.", None,"center", "10pt bold")
  tommy.goto(0,-150)
  input("Press Enter to begin I guess")
  start()

def start():
  ps.name = input("What is your name?")
  input("Hello " + ps.name + " Press Enter to Start")
  main_menu.Main_menu()
home_screen()
