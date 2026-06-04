
# RANDOM BULLSHIT GO

import random
from functools import reduce
from lib.core import even_numbers,is_even,generate_random_chars
from pprint import pprint


gola = random.sample(range(0,1000), 15)
random_numbers = [703, 650, 125, 440, 253, 54, 114, 334, 744, 530, 892, 7, 386, 438, 346]

print(list)

# filter(), map(), reduce(), zip()

#filter()



def mult_2(param):
    return param * 2

print(mult_2(10))

#efemera
square = lambda x: x * 2

print(square(10))

# filtrati toate nr multiple de 7
rez = list(filter(lambda x: x % 7 == 0, random_numbers))
print(rez)

rez1 = list(filter(is_even, random_numbers))
print(rez1)



print("\n========:Map functions:=========")
# map(), reduce(), zip()
# map() functioneaza ca un 'for'

random_numbers = [703, 650, 125, 440, 253, 54, 114, 334, 744, 530, 892, 7, 386, 438, 346]

xd = list(map(lambda x: x // 2, random_numbers))
print(xd)

var2 = list(map(lambda x: x ** 2, random_numbers))
print(var2)



print("\n========:Reduce functions:=========")
# reduce() functioneaza ca o adunare dintr-o lista

var3 = reduce(lambda x,y: x+y, random_numbers, 10000)
print(var3)

var4 = reduce(lambda x,y: x*y, random_numbers)
print(var4)
string = str(1882982066451526676913007610880000000)
print(len(string))

# random_letters = ['b', 'z', 'f', 'h', 'l', 'u', 'o']

# chr() schimba din int in character

min_txt = 97
max_txt = 122
count = 10
random_letters1 = []
step1 = random.sample(range(min_txt , max_txt + 1), count)
random_letters1 = list(map(lambda x: chr(x) , step1))


# random.shuffle(step2)
# print(step2)
# for i in range(count):
#     random_letters.append(chr(random.randint(min_txt, max_txt)))

random_letters = (generate_random_chars(97,122,10))
random_letters_japan = (generate_random_chars(12353,12447,10))



print("\n========:Zip functions:=========")
# zip() combina mai multe liste intr-un tuplu pentru fiecare. zip() combina cel mai mic numar din oricare lista
# rezultatul e o lista care poate fi facuta dictionar cu "dict (zip (list1 , list2) )"

names = ["John" , "Orion" , "Aria" , "Emre" , "Navia"]
ages = [26,33,20,29,22]

combined_list = list(zip(names , ages))
print(combined_list)

print("\n========:Key Values:=========")

score = [6,12,15,3,40]

zipped = list(zip(names, ages, score))
print(zipped)
print("\n")


people = []
for elem in zipped:
    people.append({
        "name" : elem[0],
        "age" : elem[1],
        "score" : elem[2]
    })
pprint(people,sort_dicts=False)
print("\n")

sorted_list = sorted(people, key=lambda x: x["name"])
# sorted_list = sorted(people, key=lambda a, b: a > b)
# sorted(lista,cheie,reverse True/False)



print(sorted_list)











