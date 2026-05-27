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