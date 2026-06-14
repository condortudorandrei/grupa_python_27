
# stiu ca pare foarte lung degeaba dar am facut un program care se repeta cat timp utilizatorul vrea, i guess


lista_cumparaturi = ["oua", "lapte","carne","fasole","apa minerala","banane"]  # lista.mp4

def afisare_lista(lista_cumparaturi):               # functie pentru afisare
    for element in lista_cumparaturi:
        print(f"- {element}")

def adaugare_element(lista_cumparaturi):            # functie pentru adaugare element
    elem = input("\nCe element vreti sa adaugati? : ")
    if elem in lista_cumparaturi:                               # se verifica daca elementul exista deja in lista
        print(f"\n'{elem}' exista deja in lista de cumparaturi.")
    if elem not in lista_cumparaturi:
        lista_cumparaturi.append(elem)                            # lista creste
        print(f"\n'{elem}' a fost adaugat in lista de cumparaturi.\nNoua lista de cumparaturi:")
        for element in lista_cumparaturi:                       # afisam din nou lista pentru claritate
            print(f"- {element}")

def stergere_element(lista_cumparaturi):            # functie pentru stergere element
    elem = input("\nCe element vreti sa stergeti? : ")
    if elem in lista_cumparaturi:                               # se verifica daca elementul este in lista
        lista_cumparaturi.remove(elem)                          # rip element
        print(f"\n'{elem}' a fost sters din lista.\nNoua lista de cumparaturi:")
        for element in lista_cumparaturi:                       # afisare again
            print(f"- {element}")
    else:
        print(f"\n'{elem}' nu se afla in lista de cumparaturi.")

def stergere_lista(lista_cumparaturi):                  # functie stergere
    lista_cumparaturi.clear()                                   # let me be clear
    print("Lista de cumparaturi a fost stearsa.")

def cautare_element(lista_cumparaturi):             # functie google
    elem = input("Ce element vreti sa cautati? : ")
    if elem in lista_cumparaturi:                               # verificare elem daca e in lista
        print(f"'{elem}' se afla in lista de cumparaturi.")
    else:
        print(f"'{elem}' nu se afla in lista de cumparaturi.")




                                                                # mare print
print("""                                                   

Instructiuni de utilizare
1 - Afisarea lista de cumparaturi
2 - Adaugarea element
3 - Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi
""")

# de aici e interesant

x = 1                                                       # x=1 e folosit pentru ca programul sa se repete
while x == 1:                                               # conditie pentru repetatie
    check = 0                                           # check este folosit pentu mesajul de repetitie
    try:                                                   # try/catch pentru a acoperi si imputurile de tip str
        i = int(input("\n\nIntroduceti instructiune mai jos: (1-5)\n------------------------------------------\n"))
        print("------------------------------------------")
    except ValueError:                                      # catch these hands
        i=9                                             # valoare arbitrara pentru a afisa eroarea (putea fi 321342186471 ca tot e ok)
    if i == 1:
        print("Afisarea listei de cumparaturi")
        afisare_lista(lista_cumparaturi)                # apelare functie
    elif i == 2:
        print("Adaugare element in lista de cumparaturi")
        adaugare_element(lista_cumparaturi)             # dos
    elif i == 3:
        print("Stergere element din lista de cumparaturi")
        stergere_element(lista_cumparaturi)             # troi
    elif i == 4:
        print("Stergere lista de cumparaturi")
        stergere_lista(lista_cumparaturi)               # vier
    elif i == 5:
        print("Cautare in lista de cumparaturi")
        cautare_element(lista_cumparaturi)              # пять
    else:
        print("Instructiunea nu exista! Va rugam reincercati.\n")
        check = -1                                     # se forteaza check sa fie '-1' pentru a evita un mesaj inutil
    while True:                                     # loop pentru a verifica daca input-ul de la user este y/n
        if check == -1:                             # doua randuri mai sus :)
            break
        check = input("\nDoriti sa executati alta instructiune in lista?   (y/n) : ")
        if check == "n":
            x = 0                                   # conditie pentru terminarea programului
            break
        elif check == "y":
            break                                   # daca y atunci ok
        else:
            print(f"\n{check} Nu este un input valid. Reincercati.\n")      # mesaj pentru a cere un nou imput al user-ului


