

# flow -> curge

list1 = [1,2,5,7,33,12,100]

#instructiuni elementare: for,while,if,try/catch,switch,

nr_exe = 0

for elem in range(5):
    if elem > 2 & elem < 4:
        print(list1[elem])
    nr_exe = nr_exe + 1
print("Nr executii:")
print(nr_exe)

#IF statements:
populatie_cluj = 300000
if populatie_cluj > 250000:
    print("Prea Mare")
else:
    print("Mai incape")

list2 = [6,7,10,90,100,33,88,5,13,0]
nr_pare = []
nr_impare = []

for elem in list2:
    if elem % 2 == 0:
        nr_pare.append(elem)
    else:
        nr_impare.append(elem)

print(nr_pare)
print(nr_impare)

for elem in list2:
    if elem % 2 == 0 and elem % 5 == 0:
        print(elem)










