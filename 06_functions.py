
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









