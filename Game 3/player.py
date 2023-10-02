import gear
friend = False
hp = 100
turns = 0
inventory = ["Book", "Time Spell"]
gold = 0
immune = False
dogName = ""
perTurn = 0
childrenKicked = 0
strengthSkill = 1
carName = ""

RHand = gear.empty
Head = gear.empty
Legs = gear.FarmSack
Torso = gear.FarmSack
Feet = gear.FarmSack

def strength_calc():
  weapon_Power = RHand * 0.5
  total = weapon_Power + strengthSkill -  childrenKicked * .65
  return total 
  
def defense():
  d = (Head*0.3)+(Legs*0.7)+(Torso*0.78)+(Feet*0.15)
  return d
  
strength = strength_calc()
defense = defense()