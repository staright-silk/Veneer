name=str(input("Enter your name: "))
print(f"Hello,{name.capitalize()}!")
print("You can choose 4 paths / occupations:\n"
      "1. Carpenter\n"
      "2. Doctor\n"
      "3. Fisherman\n"
      "4. Hunter")
occupation=str(input("Enter your choice of occupation: -> do not make spelling mistakes".capitalize()))
occupations=["Carpenter","Doctor","Fisherman","Hunter"]
if occupation.capitalize() in occupations:
    print("Occupation has been selected")
else:    print("Occupation has not been selected")
if occupation.capitalize() == "Carpenter":
    print("You have chosen to be a carpenter")
elif occupation.capitalize() == "Doctor":
      print("You have chosen to be a doctor")
elif occupation.capitalize() == "Fisherman":      print("You have chosen to be a fisherman")
elif occupation.capitalize() == "Hunter":
      print("You have chosen to be a hunter")

else:    print("You have not chosen an occupation")



