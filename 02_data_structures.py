# Liste v2:
print("LISTE")
list1 = [1,32,83,433,51,632314,2,69,33]
print(list1[-1])
print(len(list1))

index=len(list1)//2
print(list1[index])


list2 = [1,44,652,42,4,99,351,44,200]
print(list2)
list2[3]=100
print(list2)


print()
# Dictionare:
print("DICTIONARE")
persona = {
    "key" : "value",
    "Nume" : "Matei",
    "Inaltime" : "1.85m",
    "Varsta" : 27,
    "Cetatiean_roman" : True,
    "Bolnav" : False,
    "Greutate" : 75.7
}
print(persona)


# fast lookup
print(persona["Nume"])
persona["Varsta"] = 50
persona["CNP"] = "1980607025192"
print(persona)

print()
# seturi
print("SETURI")
elemset = {3,67,10,9,8,3}
print(elemset)

list3 = [1,33,83,433,51,632314,1,69,33]
list3_no_dupe = set(list3)
print(list3_no_dupe)


print()
# tuple, like a list but immutable.
print("TUPLE")
coordinates = (0,10)
coordinates3D = (0,15,5)
print(coordinates[1])

coordinates = (8,12)
print(coordinates[1])


print()
# Metode
print("METODE")
# catel = "Spot"
# catel.latra("Pipoi")
# catel.mananca("Lasagna")
# catel.miroase("Andrei")
# catel.musca("Andrei")
#obiect.actiune/functie/metoda (parametrii)

list5 = [7,8,100,99]
list5.append(-50)
list5.pop(1)
list5.reverse()
list5.sort()
print(list5)

set2 = {7,8,5,6,100,99,8}
set2.add(-5)
set2.remove(8)
print(set2)


print()
#chei de dictionare
#cheile pot fi orice str,int,float,bool,tuple,dict
print("CHEI DE DICTIONARE")
dict_2 = {
    "key": "value",
    1: "one",
    3.14: "PI",
    True: False,
    (2,3): "coordinates",
    "bizar":{
        "level2":{
            "lsit6": [0,1,2,3,4,6,7,9,3]
        }
    }
}
print(dict_2)










