
# RANDOM BULLSHIT GO

import random
from lib.core import even_numbers,is_even



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