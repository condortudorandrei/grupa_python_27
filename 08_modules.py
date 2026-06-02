
import os
# OS interractions

# print(os.getcwd())
# print(os.listdir())
#
# if os.path.exists("manage.py"):
#     print("DA")
#     print(os.path.getsize("manage.py"))
# else:
#     print("NU")

# os.path.listdir() returneaza o lista de nume de foldere si fisiere
# os.path.isfile(fisier) returneaza True daca "fisier" este un fisier.
# os.path.getsize(fisier) returneaza marimea fisierului.

# Ex.: Creati o functie care trece prin fisierele din folderul curent si returneaza marimea totala a fisierelor

list = os.listdir()
def file_size(list):
    """
    Function that returns total file size in root level directory
    :return: total file size in KB
    """
    suma = 0
    for elem in list:
        if os.path.isfile(elem) == True:
            print(elem)
            suma = suma + os.path.getsize(elem)
    return(suma) / 1024
print (file_size(list))








