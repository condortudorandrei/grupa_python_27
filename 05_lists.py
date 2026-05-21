
# variabile prin referinta
list1 = [10,30,5,7,100,-5]
list2 = list1
print(list1)
list2.append(81)
print(list1)

# variabile prin valoare
var1 = 100
var2 = var1
var2 = 77
print(var2)

list3 = [9,10,100,5,50,4]
#slicing,splicing
#syntax: list[start:stop:step]
print(list3[0:6:2])

list4 = list3[:]
list4.append(1335)
if list4 == list3:
    print("DA")
else:
    print("NU")

list5 = [list3[3],list3[1]]
print(list5)
list5.append(99)
list5.extend([100,101,102])
list5 += [105,104,103]
print(list5)
list5.remove(100) #sterge doar primul 100 intalnit in lista.
print(list5.index(99))
list5.sort()
print(list5)
list6 = sorted(list5) # folosit pentru a mentine lista intiala la fel


#MATRICI
print()
print("MATRICI")
matrice1 = [
    [3,4,10],
    [7,8,10],
    [0,3,99]
]
print(matrice1)

#list comprehention
list7 = [3,4,5]
list8 = [x ** 3 for x in list7]
print(list8)

list9 = [x ** 3 for x in list7 if x % 2 == 0]
print(list9)

#STRINGURI
print()
print("STRINGURI")

#un string se comporta ca o lista imutabila
alfabet = "ABCdefghijklmnopqrstuvwxyz"
print(alfabet)
print(alfabet[25])
print(alfabet[::-1])
print(alfabet[::2].upper())
print(alfabet.replace("f","1"))
prop1 = "Ana are mere, Ana a gasit doua mere, Ana mananca mere."
print(prop1)
print(prop1.split(","))
list10 = (prop1.split(","))
print(list10[0])

var3 = ["a","b","c","pneumonoultreamicroscopicsilicovulcaniconioza","deutre D3"]
rezultat1 = "-".join(var3)
print(rezultat1)

if("D3" in rezultat1):
    print("avem vitamine")

ex1 = "AVG-JRD-IOR:RED-GRN-BLU:QWE-RTY-UIO"
#luati acest string si creati o matrice 3x3, in care sa pastrati doar literele
rezultat3 = []
part1 = ex1.split(":")
for elem in part1:
    print(elem)
    rezultat3.append(elem.split("-"))
print(rezultat3)

print(rezultat3[1][0])

# while
for i in range(4):
    print(i)
i=0
while i<4:
    print(i)
    i=i+1

list11 = [10,202,300,100]

while True:
    print(list11.pop(0))
    if len(list11) <= 0:
        break



#formatare
#f-string

name = "Alex"
age = 27
profession = "Carpenter"

print("Hello name is " + str(name) + " age is " + str(age) + " profession is " + str(profession))
print(f"Hello name is {name} age is {age} profession is {profession}")
print("Hello name is {} age is {} profession is {}".format(name,age,profession))

#multi-line message foloseste """""" (6x") (6 ghilimele)
msg1 = "Line 1 \nLine 2"
print (msg1)

msg2 = """
coka
p           enelopa
    loca 
"""
print(msg2)





















