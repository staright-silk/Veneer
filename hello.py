import carpenter
import doctor
import fisherman
import hunter
import time
import sys
import time

def type_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def type_input(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return input()
name = input("Enter your name: ")
print(f"Hello, {name.capitalize()}!")

print(
    "You can choose 4 paths / occupations:\n"
    "1. Carpenter\n"
    "2. Doctor\n"
    "3. Fisherman\n"
    "4. Hunter"
)

occupation = type_input("Enter your choice of occupation: ")
occupations = ["Carpenter", "Doctor", "Fisherman", "Hunter"]

if occupation.capitalize() in occupations:
    print("Occupation has been selected")
    
    if occupation.capitalize() == "Carpenter":
        carpenter.carp_start()
    elif occupation.capitalize() == "Doctor":
        doctor.doc_start()
    elif occupation.capitalize() == "Fisherman":
        fisherman.fisher_start()
    elif occupation.capitalize() == "Hunter":
        hunter.hunt_start()
else:
    print("Occupation has not been selected")

time.sleep(2)



type_print("\nYou arrive at Moonfall Town. \nAs you look up at the glistening sky, you see stars shining like white pearls.\nThe trees bordering the side of the road are laced with beautiful strings of glowing unknown material, seems natural. \nIt is a lively town, the townsfolk are chattering and are having a good time. \nYou smile at yourself as you feel a sense of belonging.")

input("\n[Press Enter to continue...]")

type_print("\nAs you walk through the town, you see a group of children running about. \nThey are laughing and splashing water at each other. \nYou can't help but smile at their innocence and joy. \nYou continue walking and see a market bustling with activity. \nVendors are selling fresh produce, handmade crafts, and delicious food. \nThe aroma of freshly baked bread fills the air, making your stomach growl.")

input("\n[Press Enter to continue...]")

type_print("\nYou decide to stop by a bakery and buy a loaf of bread. \nThe baker greets you warmly and offers you a sample of their latest creation, a sweet pastry filled with fruit. \nYou take a bite and savor the delicious flavors. \nYou thank the baker and continue on your way, feeling grateful for the simple pleasures in life.")


time.sleep(1.5)

health = 100
stamina = 50

x = type_input("\nYou think whether to take rest or not \nat the nearby cabin, The Glade Of Sien.\n\nYes or No?: ")

if x.strip().lower() in ['yes', 'y']:
    type_print("\nYou decided to rest at The Glade Of Sien.")
    stamina = min(100, stamina + 30)
    print(f"Stamina recovered! Current Stamina: {stamina}, Health: {health}")
elif x.strip().lower() in ['no', 'n']:
    type_print("\nYou decided to keep moving.")
    stamina = max(0, stamina - 20)
    health = max(0, health - 5)
    type_print(f"You grow very tired. \nYour head feels dizzy and you slump to the ground as your consciousness fades away.")
    type_print(f"Current Stamina: {stamina}, Health: {health}")
          
else:
    type_print("\nInvalid choice! Please type Yes or No.")

