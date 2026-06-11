
import os
import json

from pathlib import Path

from pprint import pprint

# deschidem un stream catre acel fishier:
f = open("input_file.json", "r", encoding="utf-8")
print(f)

#citim fisierul:

content = f.read()
print(content)

print("citim iar fisierul:\n")

content2 = f.read()
print(content2)

f.close()

print("======== Proper file reading: =======")

# altfel de citire
with open("input_file.json", "r", encoding="utf-8") as f:
    lines = f.readlines()
    pprint(lines)
    #f.close() se face automat la sfarsitul acestui "with"



print("======== Next file chapter: =========")

output_data = {
    "data": [50,100,300,"hello","ඞ"],
    "title": "dhwqiuhgrfqkl",
    "author": "Dani Mocanu",
    "AMOGUS": ["ඞ","ඞ","ඞ","ඞ","ඞ","ඞ"]
}

file_name = "output_file.json"

def write_data(file_name,data):
    path = Path(file_name)
    path.parent.mkdir(parents=True, exist_ok=True)
    # write data to file
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        print("Data saved succesfully!")

write_data(file_name,output_data)


def read_data(file_name,data):
    path = Path(file_name)
    path.parent.mkdir(parents=True, exist_ok=True)
    # READ NIGGA, READ!
    with open(path, "r", encoding="utf-8") as f:
        pprint(f.read())
read_data(file_name,output_data)


# with open(path, "r", encoding="utf-8") as f:
#     data = json.load(f)
# pprint(data)












