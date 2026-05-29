import carpenter
import doctor
import fisherman
import hunter

name = input("Enter your name: ")

print(f"Hello, {name.capitalize()}!")

print(
    "You can choose 4 paths / occupations:\n"
    "1. Carpenter\n"
    "2. Doctor\n"
    "3. Fisherman\n"
    "4. Hunter"
)

occupation = input(
    "Enter your choice of occupation: "
)

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


print("You arrive at Moonfall Town. \nAs you look up at the glistening sky, you see stars shining like white pearls.\n The trees bordering the side of the road are laced with beautiful strings of glowing unknown material, seems natural. \n It is a lively town, the townsfolk are chattering and are having a good time. \n You smile at yourself as you feel a sense of belonging.")
print ("As you walk through the town, you see a group of children running about. \n They are laughing and splashing water at each other. \n You can't help but smile at their innocence and joy. \n You continue walking and see a market bustling with activity. \n Vendors are selling fresh produce, handmade crafts, and delicious food. \n The aroma of freshly baked bread fills the air, making your stomach growl.")
print ("You decide to stop by a bakery and buy a loaf of bread. \n The baker greets you warmly and offers you a sample of their latest creation, a sweet pastry filled with fruit. \n You take a bite and savor the delicious flavors. \n You thank the baker and continue on your way, feeling grateful for the simple pleasures in life.")
health = 100
stamina = 50

x = input("You think whether to take rest or not \n at the nearby cabin, The Glade Of Sien.\n\n Yes or No?: ")

if x.strip().lower() in ['yes', 'y']:
    print("You decided to rest at The Glade Of Sien.")
    stamina += 30
    print(f"Stamina recovered! Current Stamina: {stamina}, Health: {health}")
elif x.strip().lower() in ['no', 'n']:
    print("You decided to keep moving.")
    stamina -= 20
    health -= 5
    print(f"You grew tired. Current Stamina: {stamina}, Health: {health}")
else:
    print("Invalid choice! Please type Yes or No.")
