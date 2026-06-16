
from pprint import pprint

def object_constructor(name,owner,temperament = "loving"):
    new_object = {
        "name": name,
        "owner": owner,
        "temperament": temperament
    }
    return new_object

cat1 = object_constructor("Shadow",owner = "Feri")
cat2 = object_constructor("Paw",owner = "Lydia",temperament = "Feral")

pprint(cat2)

cat3 = cat2

cat3["temperament"] = "Shy"

pprint(cat2)

cat4 = cat3.copy()
cat4["name"] = "dhueaui"


print(cat3)









