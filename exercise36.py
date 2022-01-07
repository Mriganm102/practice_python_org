import json
from bokeh.plotting import figure, show, output_file
from collections import Counter
output_file("bokeh.html")
with open("info.json", "r") as f:
    info = json.load(f)
info1 = []
def months(name):
    months_list = ["January", "Febraury", "March", "April", "May", "June", "July", "August", "September", "October",
                   "November", "December"]
    for i in months_list:
        if i in info[name]:
            info1.append(i)
months("Benjamin Franklin")
months("Albert Einstein")
months("Ada Lovelace")
print(info1)
info2 = Counter(info1)
print(info2)
list1 = []
for x in info2:
    y = (info2[x])
    list1.append(y)
print(list1)
p = figure()
p.vbar(x=info1, top=list(list1), width=0.5)
show(p)


