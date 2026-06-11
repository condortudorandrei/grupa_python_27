from pprint import pprint

def filtrare(cetateni):                                    # doar o lista ca si parametru
    lista_filtrata = []                                              # adaugat o lista goala pentru rezultat
    for elem in cetateni:                                            # conditie for
        if elem["Varsta"] > 25 and elem["Greutate"] >60:             # conditie.exe
            lista_filtrata.append(elem)                              # adaugat in a doua lista
    return lista_filtrata                                            # return (prima data am scris print si nu stiam de ce nu merge :')



cetateni = [                                                        # initializare_lista.mp4
    {
        "CNP": 19304843895738,
        "Nume": "Marius Moga",
        "Varsta": 32,
        "Adresa": "Brasov, Jud Brasov",
        "Greutate": 75,
    },
    {
        "CNP": 195048438345345,
        "Nume": "Matei Luca",
        "Varsta": 30,
        "Greutate": 59
    },
    {
        "CNP": 193048438111111,
        "Nume": "Ana Popescu",
        "Varsta": 24,
        "Greutate": 65
    },
    {
        "CNP": 193048438222222,
        "Nume": "Ioana Ionescu",
        "Varsta": 28,
        "Greutate": 62
    },
    {
        "CNP": 193048438333333,
        "Nume": "George Marin",
        "Varsta": 40,
        "Greutate": 85
    }
]
pprint(filtrare(cetateni))                                          # pprint ca stim sa scriem






