
# functii
# def == keyword, face parte din sintaxa de definire a unei functii


def greet():
    print("hello")
    print("text foarte lung si inutil")


#apelare de functie
greet()


# add

def add(a, b):
    return a+b

add(25,2321321)

# suma(25,2321321)

def mul(a, b):
    return a*b


print(mul(3,5))

print(add(mul(3,15),20))

var1 = mul(5,15)
print(add(var1,mul(5,15)))

# parametru se numeste acel "a". Argument este valoarea ce o dam acelui "a", ex:5

#creati sub, care scade a-b, div (a/b) si pow (a**b)

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def pow(a,b):
    return a**b

rez = add(5 , mul(4 , pow(8,2)))

print(rez)

#return implicit, None

def speak(word="Woof!"):
    print(word)

speak()
speak("Miau")

def drive(car_model, max_speed=130):
    print(f"{car_model} is running at a max speed of {max_speed}kmph")

drive("Audi")
drive("Mazda", "RED") #????????????????????????????????


def mod(a: int , b: int):
    """
    Scurta descriere
    :param a: number devided by
    :param b: number devided with
    :return: result
    """
    return a%b


print(mod(5,3))


nr = [10,11,21,5,-1,20,3]

def even_numbers(list):
    phlist = []
    for num in list:
        if mod(num,2) == 0:
            phlist.append(num)
    return phlist

print(even_numbers(nr))

list_1 = ["ERR-Value Error-ER:10" , "INF-Program launch Info-CD:5" , "WRN-Low memory-WR:11"]

print("tema procesare stringuri")

def format_logs(list):
    for elem1 in list:
        lista = elem1.split("-")                                                                    # split la lista dupa '-' ca sa avem datele importante (codul de eroare si mesajul
        listb = elem1.split(":")                                                                    # split la lista dupa ':' pentru a avea ultimul numar
        print()
        if lista[0] == "ERR":                                                                       # conditie pentru "ERR"
            print(f"[ERROR] \nMesaj : {lista[1]} \nCod: {listb[1]}" )
        elif lista[0] == "INF":                                                                       # conditie pentru "INF"
            print(f"[INFO] \nMesaj : {lista[1]} \nCod: {listb[1]}")
        elif lista[0] == "WRN":                                                                       # conditie pentru "WRN"
            print(f"[WARNING] \nMesaj : {lista[1]} \nCod: {listb[1]}")
        else:
            print(f"Invalid Format: \nNo 'ERR', 'INF' or 'WRN' found.")

format_logs(list_1)



# refactorizare
# schimbare de pe "print" pe "return"


# def format_logs(place_holder):
#     for elem1 in place_holder:
#         lista = elem1.split("-")
#         listb = elem1.split(":")
#         chunks = []
#         print()
#         if lista[0] == "ERR":
#             chunks.append("[ERROR] \nMesaj : {lista[1]} \nCod: {listb[1]} \n")
#         elif lista[0] == "INF":
#             chunks.append("[INFO] \nMesaj : {lista[1]} \nCod: {listb[1]} \n")
#         elif lista[0] == "WRN":
#             chunks.append("[WARNING] \nMesaj : {lista[1]} \nCod: {listb[1]} \n")
#         else:
#             return("Invalid Format: \nNo 'ERR', 'INF' or 'WRN' found.")
#     strings = "\n".join(chunks)
#     return strings
# print(format_logs(list_1))

























