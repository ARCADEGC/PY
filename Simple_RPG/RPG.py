import os
import time
import csv
import random

def mob_generator(type):
    enemy_types = {
            1: "Reaper",
            2: "Clone",
            3: "Emperor",
            4: "Ghost",
        }
    return enemy_types.get(type, "Postbone")

def save():
    with open("inventory.csv", "w", newline = "") as csvfile:
        writer = csv.writer(csvfile, delimiter = ",")
        set_row = 0
        while set_row <= len(inventory):
            writer.writerow([inventory[set_row]])
            set_row += 1

def drop_chance(level):
    chance = random.randint(1, int(round(level / 2))) if level >= 2 else random.randint(1, 2)
    return "True" if chance == 1 else "False"

#inventory [(1) headgear 0, (1) chestgear 1, (1) pants 2, (1) boots 3, (1) weapon 4, (1) shield 5, (1) level 6, (100) health 7, (10) potions 8, () weapon damage 9, (0) xp 10, (100) money 11]
inventory = []
with open("inventory.csv", "r") as csvfile:
        gear = csv.reader(csvfile, delimiter = ",")
        for data in gear:
            inventory.append(str(data[0]))

os.system("cls")
print("""
          _____            _____                    _____                    _____          
         /\    \          /\    \                  /\    \                  /\    \         
        /::\____\        /::\    \                /::\    \                /::\    \        
       /:::/    /       /::::\    \              /::::\    \              /::::\    \       
      /:::/    /       /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/    /       /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/    /       /:::/__\:::\    \        /:::/__\:::\    \        /:::/  \:::\    \    
   /:::/    /       /::::\   \:::\    \      /::::\   \:::\    \      /:::/    \:::\    \   
  /:::/    /       /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \  
 /:::/    /       /:::/\:::\   \:::\____\  /:::/\:::\   \:::\____\  /:::/    /   \:::\ ___\ 
/:::/____/       /:::/  \:::\   \:::|    |/:::/  \:::\   \:::|    |/:::/____/  ___\:::|    |
\:::\    \       \::/   |::::\  /:::|____|\::/    \:::\  /:::|____|\:::\    \ /\  /:::|____|
 \:::\    \       \/____|:::::\/:::/    /  \/_____/\:::\/:::/    /  \:::\    /::\ \::/    / 
  \:::\    \            |:::::::::/    /            \::::::/    /    \:::\   \:::\ \/____/  
   \:::\    \           |::|\::::/    /              \::::/    /      \:::\   \:::\____\    
    \:::\    \          |::| \::/____/                \::/____/        \:::\  /:::/    /    
     \:::\    \         |::|  ~|                       ~~               \:::\/:::/    /     
      \:::\    \        |::|   |                                         \::::::/    /      
       \:::\____\       \::|   |                                          \::::/    /       
        \::/    /        \:|   |                                           \::/____/        
         \/____/          \|___|                                                            
""")

#start
start = input("\n\n\t (y/n) Do you want to play: ")
if start == "y":
    run = 1
else:
    run = 0
os.system("cls")

while run == 1:

    #mob level
    mob_level = int(inventory[6])

    #set what to do
    game_state = input("\n\t (Fight / Market / Exit / Save / Inventory) \n\n\t What do you want to do? ")
    if game_state == "f":

        os.system("cls")
        mob = mob_generator(random.randint(1, 5))
        mob_health = 100 * mob_level
        print(f"\n\t Your mob is {mob}!")

        time.sleep(1)
        os.system("cls")

        print(f"\n\t {mob}s health is {mob_health} \n\t Your health is {inventory[7]}")        

        fight = 1
        while fight == 1:

            critical = random.randint(1, 10)
            if critical == 10:
                inventory[9] = int(inventory[4]) * 20
            else:
                inventory[9] = int(inventory[4]) * 10

            strike = input(f"\n\t /Damage {inventory[9]}/ (f/p/r) Fight with level {inventory[4]} weapon / Use a Potion to restore {(10 * int(inventory[6]))} ({inventory[8]}) / Flee? ")
            if strike == "f":
                mob_health -= int(inventory[9])
            elif strike == "p":
                if int(inventory[8]) > 0:
                    inventory[8] = int(inventory[8]) - 1
                    inventory[7] = int(inventory[7]) + (10 * int(inventory[6]))
            elif strike == "r":
                flee_chance = random.randint(1, 3)
                if flee_chance == 3:
                    os.system("cls")
                    print("\n\t You run away! ")
                    time.sleep(1)
                    fight = 0
                    break
                else:
                    print("\n\t The enemy stopped you! ")
                    time.sleep(1)                    
            os.system("cls")

            if int(mob_health) <= 0:

                os.system("cls")

                inventory[10] = int(inventory[10]) + 10
                droped_money = int(10 * (int(inventory[6]) * 0.5))
                inventory[11] = int(inventory[11]) + droped_money
                if int(inventory[10]) >= int(inventory[6]) * 10:
                    inventory[10] = 0
                    if int(inventory[6]) < 10:
                        inventory[6] = int(inventory[6]) + 1 
                print(f"\n\t You got 10xp & {droped_money}$!")

                chance = drop_chance(int(inventory[6]))
                if chance == "True":
                    item_index = {"Reaper": 0, "Clone": 1, "Emperor": 2, "Ghost": 3, "Postbone": 5}[mob]
                    if int(inventory[item_index]) < int(inventory[6]):
                        inventory[item_index] = int(inventory[item_index]) + 1
                        print("\n\t You found a new {}!".format(["Headgear", "Chestwear", "Pants", "Boots", "Shield"][item_index]))

                fight = 0

            if fight == 1:

                mob_damage = round(((mob_level * random.randint(1, 5)) / 100) * (100 - (int(inventory[0]) * 1) - (int(inventory[1]) * 1) - (int(inventory[2]) * 1) - (int(inventory[3]) * 1) - (int(inventory[5]) * 2)))

                print(f"\n\t {mob} attacks with {mob_damage}")
                inventory[7] = int(inventory[7]) - mob_damage
                first_enemy_hit = 1

                print(f"\n\t {mob}s health is {mob_health}, \n\t Your health is {inventory[7]}!")

                if int(inventory[7]) <= 0:
                    run = 0
                    break
    elif game_state == "m":
        shopping = 1
        os.system("cls")
        while shopping == 1:
            sword_cost = pow(int(inventory[4]), 2)
            purchase = input(f"\n\t ({inventory[11]}$) (S/P/L) Do you want to buy a Sword ({sword_cost}$), Potions (3 for 10$) or do you want to leave? ")
            if purchase == "s":
                if int(inventory[6]) > int(inventory[4]):
                    if int(inventory[11]) >= sword_cost:
                        inventory[4] = int(inventory[4]) + 1
                        inventory[11] = int(inventory[11]) - sword_cost
                        print(f"\n\t You bought a new Sword for {sword_cost}$!")
                        time.sleep(1)
                        os.system("cls")
                    else:
                        print("\n\t You dont have anough money! ")
                        os.system("cls")
                else:
                    print("\n\t You need to be higher level to purchase this Weapon! ")
                    time.sleep(1)
                    os.system("cls")
            elif purchase == "p":
                if int(inventory[11]) >= 10:
                    inventory[8] = int(inventory[8]) + 3
                    inventory[11] = int(inventory[11]) - 10
                    print(f"\n\t You bought 3 Potions for 10$!")
                    time.sleep(0.5)
                    os.system("cls")
                else:
                    print("\n\t You dont have enough money! ")
                    os.system("cls")
            elif purchase == "l":
                os.system("cls")
                shopping = 0
                break
            else:
                os.system("cls")
    elif game_state == "e":
        os.system("cls")
        two_step = input("\n\t (y/n) Are you sure you want to leave & save? ")
        if two_step == "y":
            save()
            run = 0
    elif game_state == "s":
        save()
    elif game_state == "i":
        os.system("cls")
        print(f"\n\t Your Headgear level is {inventory[0]}.")
        print(f"\t Your Chestgear level is {inventory[1]}.")
        print(f"\t Your Pants level is {inventory[2]}.")
        print(f"\t Your Boots level is {inventory[3]}.")
        print(f"\t Your Weapon level is {inventory[4]}.")
        print(f"\t Your Shield level is {inventory[5]}.")
        print(f"\t Your Level is {inventory[6]}.")
        print(f"\t Your Health is {inventory[7]}.")
        print(f"\t You have {inventory[8]} Potions.")
        print(f"\t You have {inventory[10]}xp.")
        print(f"\t You have {inventory[11]}$.")        
    else:
        os.system("cls")

print("\n\n END!")