import json
from collections import Counter

with open("info.json", "r") as f:
    info = json.load(f)
info1 = []
birthday_counter = Counter(info)
months_list = ["January", "Febraury", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]

def months(name):
    for x in months_list:
        if x in info[name]:
            info1.append(x)
months("Benjamin Franklin")
months("Albert Einstein")
months("Ada Lovelace")
info1 = Counter(info1)
print(info1)
