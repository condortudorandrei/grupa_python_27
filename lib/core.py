import random

def even_numbers(list):
    phlist = []
    for num in list:
        if num % 2 == 0:
            phlist.append(num)
    return phlist




def odd_numbers(list):
    phlist = []
    for num in list:
        if num % 2 != 0:
            phlist.append(num)
    return phlist


def is_even(nr):
    return nr % 2 == 0


def generate_random_chars(min_txt = 97, max_txt = 122, count = 10):
    random_letters = []
    step1 = random.sample(range(min_txt, max_txt + 1), count)
    random_letters = list(map(lambda x: chr(x), step1))
    return(random_letters)



