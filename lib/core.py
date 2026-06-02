

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






