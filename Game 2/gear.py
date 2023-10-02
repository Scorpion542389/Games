import ps
FarmKnife = 2.2
empty = 0
FarmSack = 0
Short_sword = 2.5
Sword = 2.75
Knights_Sword = 3
Mithril = 5
Omega = 100
Iron_plated = 3
Steel_plated = 3.5
Copper = 2.85
Light = 1
Heavy = 1.5
Gold_lined = 2.95

RHand = empty
Head = empty
Legs = FarmSack
Torso = FarmSack
Feet = FarmSack

def strength_calc():
  weapon_Power = RHand * 0.5
  total = weapon_Power + ps.Strength_skill + ps.level*.65
  return total 
  
def defense():
  d = (Head*0.3)+(Legs*0.7)+(Torso*0.78)+(Feet*0.15)
  return d
  
treasure_armor = [Mithril,Iron_plated,Steel_plated,Copper,Light,Heavy,Gold_lined]
tanames = ["Mithril","Iron Plated","Steel Plated", "Copper","Light","Heavy","Gold Lined"]

treasure_weapon = [FarmKnife,Short_sword,Sword,Knights_Sword,Mithril,Copper,Gold_lined]
twnames = ["Farm Knife","Short Sword","Broad Sword","Knight's Sword","Mithril","Copper","Gold Lined"]


