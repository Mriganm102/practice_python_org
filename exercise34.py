import json

with open("info.json", "r") as f:
    info = json.load(f)



def birthdays():
    user_input = input("Whose Birthday do you want to find out?")
    if user_input == "Albert Einstein":
        print(info["Albert Einstein"])
    elif user_input == "Benjamin Franklin":
        print(info["Benjamin Franklin"])
    elif user_input == "Ada Lovelace":
        print(info["Ada Lovelace"])
    else:
        print("Not Aplicable")
        birthdays()
birthdays()