from random import randint,random
class Location:
  def __init__(self,name,exposure):
    self.name = name
    self.exposure = exposure
    
class Store:
  def __init__(self,itemOne,itemTwo,itemThree):
    self.itemOne = itemOne
    self.itemTwo = itemTwo
    self.itemThree = itemThree


items ={
  "Pumpkin":5,
  "Key":350,
  "Wishing Coin":125,
  "Medecine":50,
}

Field = Location("Field",randint(30,50)/100)
Cave = Location("Cave",randint(10,30)/100)
mHouse = Location("Mystery House",randint(60,100)/100) #Special Location
Shop = Location("Shop",randint(1,20)/100) #Spec
wishWell = Location("Wishing Well",randint(45,85)/100) #Spec
