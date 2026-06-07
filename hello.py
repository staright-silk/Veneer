import json
import os
import carpenter
import doctor
import fisherman
import hunter
import time
import sys
import time

def main_menu():
    print("\n=== LEGENDS OF ELWEN ===")
    print("1. New Game")
    print("2. Load Game")
    print("3. Exit")

    choice = input("Choice: ")

    return choice

choice = main_menu()

if choice == "1":
    player = {
        "name": input("Enter your name: "),
        "occupation": "",
        "health": 100,
        "stamina": 50,
        "food": 10,
        "tharni": 50,
        "checkpoint": 0
    }

elif choice == "2":
    player = load_game()

    if player is None:
        print("No save file found.")
        quit()

    print(f"Welcome back, {player['name']}!")

else:
    quit()

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

def printh(text, delay = 0.063):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    
x = type_input("\nYou think whether to take rest or not \nat the nearby cabin, The Glade Of Sien.\n\nYes or No?: ")

if x.strip().lower() in ['yes', 'y']:
    type_print("\nYou decided to rest at The Glade Of Sien.")
    stamina = min(100, stamina + 30)
    print(f"Stamina recovered! Current Stamina: {stamina}, Health: {health}")
    printh("You wake up at the cabin, groggily and squint your eyes. \n You look around and see the sun shining through the window, casting a warm glow on the wooden walls. \n You stretch your arms and legs, feeling refreshed and rejuvenated. \n You step outside and take a deep breath of the fresh air.")
elif x.strip().lower() in ['no', 'n']:
    type_print("\nYou decided to keep moving.")
    stamina = max(0, stamina - 20)
    health = max(0, health - 5)
    type_print(f"You grow very tired. \nYour head feels dizzy and you slump to the ground as your consciousness fades away.")
    type_print(f"Current Stamina: {stamina}, Health: {health}")
    type_print("You wake up a few hours later, feeling weak and disoriented. \n You look around and see that you are lying on the side of the road, with a few concerned townsfolk gathered around you. \n They offer you some water and help you to your feet, but you know that you need to find a place to rest soon.")
    type_print("You continue walking, but you can feel your energy draining away. ")
          
else:
    type_print("\nInvalid choice! Please type Yes or No.")

food=10
tharni=50
printh("You currently have 10 weights of Food left.")
choice1=type_input("You decide that for the journey ahead, you need to stock up on some food and weaponry. But you only have 50 Tharni, what do you choose? ".capitalize())
if choice1.strip().lower() == "food":
    printh(f"You purchased 20 bread and 5 jars of jam! Nice Choice! You have  {tharni -50} Tharni and You have {food + 60} left!")
if choice1.strip().lower() == "weapon" or choice1.strip().lower() == "weaponry":
    printh(f"You purchased 5 weapons! Nice Choice")
    choice2=type_input("You feel very hungry. Do you want to eat some food? Yes or No? Do ".capitalize())
    if choice2.strip().lower() in ['yes', 'y']:
        food = max(0, food - 5)
        health = min(100, health + 20)
        type_print(f"You eat some food and feel rejuvenated! Current Food: {food}, Health: {health}")
    elif choice2.strip().lower() in ['no', 'n']:
        type_print("\nYou decided not to eat. You continue on your journey, but you can feel your energy draining away.")
        stamina = max(0, stamina - 10)
        health = max(0, health - 5)
        type_print(f"Current Stamina: {stamina}, Health: {health}")
    else:
        type_print("\nInvalid choice! Please type Yes or No.")
        
printh("As you continue your journey through the wilds of Elwen, you wander out of Moonfall \n, unknowingly as you chase a beautiful butterfly that was momentarily fluttering above your head.")
printh("At first the scenery seems beautiful as you run through fields full of green grass, stretching on and on till yonder \n ,the emerald green of the grass spreading everywhere.")