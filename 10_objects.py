from pprint import pprint

var1 = 10
var1 = 30 + 20
print(var1)
print(type(var1))

var2= True
var3 = var1 + var2
print(var3)

obj1 = {
    "name" : "Ion",
}
obj1["age"] = 32
obj1["cnp"] = 1980607125865
obj1["cetatenie_romana"] = var2

pprint(obj1)

list1 = []
list1.append(10)



def speak(param1 = "Hello!"):
    print(param1)
# creez o functie noua care se poate apela din obj1
# obj1.speak = speak
# aceasta functie poate acum sa fie apelata din obj1
# obj1["speak"]() -> astfel se apelaza acea functie
speak(obj1["cnp"])

# Creez o functie noua care se poate apela din obj1
#obj1.speak=speak
obj1["speak"] = speak



obj1["speak"](obj1["age"])
obj1["note"] = [7,10,4]

pprint(obj1)
# Task: Creaza un obiect similar cu obj1, cu proprietati la fel, dar valori diferite. De ex, sa aiba age=40

# task: creaza un obiect similar cu obj1, cu prop la fel dar val diferite




obj2 = obj1.copy()


obj2["age"] = 40
pprint(obj2)

obj3 = {
    "age": 50,
    "name": "Ahmed",
    "cnp": "1235895123544",
    "cetatenie_romana": False
}
obj3["speak"] = speak


# definim o functie care poate crea oricate obiecte, cu o structura fixa, cum sunt obiectele de mai sus.
# acestui nou obiect ii dam si acea functie speak
def object_constructor(name,age,cnp,cetatenie_romana):
    new_object = {"name": name, "age" : age, "cnp": cnp, "cetatenie_romana": cetatenie_romana}
    new_object["speak"] = speak
    return new_object

obj4 = object_constructor("Vlad",34,4143674831,True)
pprint(obj4)
obj4["speak"]("Hello!")


# param_obj poate fi orice variabila din exteriorul functiei, si daca are acea proprietate "age", se mareste cu 1 acel age
def do_work(param_obj):
    print("Work work work")
    param_obj["age"] = param_obj["age"]+1
    return 42



obj4["do_work"] = do_work
# apeland do_work(obj4), fiindca am pus obj4 in parametrii, atunci acelui obj4 i se modifica "age"-ul
obj4["do_work"](obj4)
pprint(obj4)



# aceasta functie poate modifica variabile si obiecte din exteriorul ei, daca primeste acel obiect ca parametru.
def grow(param1):
    param1["size"] = param1["size"] + 1
var4 = {"size":5}
grow(var4)
grow(var4)
grow(var4)
grow(var4)

pprint(var4)

# creem o functie care adauga o proprietate intr-un dict
# obj_param este referinta in memorie a acelui dicitionar
def set_hobby(obj_param,key,value):
    obj_param[key] = value

# functia altereaza obiectul chiar daca nu avem un return.
obj5 = {"name": "John Wick"}
set_hobby(obj5,"hobby","killing")
pprint(obj5)

#exemplu cu liste

def add_person(param_list,person):
    if len(person)>2:
        param_list.append(person)
        param_list.sort()
    else:
        print(f"Name needs to be 3 character or longer, and {person} does not fulfill the requirement")


lista_persoane = ["John Wick", "Winston", "Daisy"]
add_person(lista_persoane,"Cassian")
add_person(lista_persoane,"X")
add_person(lista_persoane,"Cn")
add_person(lista_persoane,"Josef")
print(lista_persoane)

lista_persoane2 = []
add_person(lista_persoane2,"Ion")
add_person(lista_persoane2,"Cristi")
add_person(lista_persoane2,"Vasile")
add_person(lista_persoane2,"Marius")
print(lista_persoane2)

# exemplu de functie care manipuleaza mai multe tipuri de date
def add_to_database(database, village, people):
    database[village] = people.copy()

database = {}
add_to_database(database,"Poienari",lista_persoane2)
add_to_database(database,"Urlati",lista_persoane)
lista_persoane2.append("Ghita")

pprint(database)





