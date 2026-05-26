
# Am incercat de 3 ori sa incarc tema asta pe GitHub...
# Initializarea listelor si adaugarea listelor care vor fi folosite ca si variable
list_main = []                                                                                      # lista principala care le tine pe ambele
list_1 = ["ERR-Value Error-ER:10" , "INF-Program launch Info-CD:5" , "WRN-Low memory-WR:11"]        # lista 1
list_2 = ["INF-Program exit-CD:14" , "WRN-Low disk space-WR:99" , "WRN-Bandwith reached-WR:87"]     # lista 2
list_main.insert(0,list_1)                                                                    # adaugam lista 1 in cea principala
list_main.insert(1,list_2)                                                                    # adaugam lista 2 in cea principala
lista = []                                                                                          # initialista variabile 1
listb = []                                                                                          # initialista variabile 2

for elem in list_main:                                                                              # folosim mai multe for-uri pentru a putea fii folosit in mai multe exemple formatate similar
    print("\n")                                                                                     # punem endline pentru aspect
    for elem1 in elem:
        lista = elem1.split("-")                                                                    # split la lista dupa '-' ca sa avem datele importante (codul de eroare si mesajul
        listb = elem1.split(":")                                                                    # split la lista dupa ':' pentru a avea ultimul numar
        print()
        if lista[0] == "ERR":                                                                       # conditie pentru "ERR"
            print(f"[ERROR] \nMesaj : {lista[1]} \nCod: {listb[1]}" )
        if lista[0] == "INF":                                                                       # conditie pentru "INF"
            print(f"[INFO] \nMesaj : {lista[1]} \nCod: {listb[1]}")
        if lista[0] == "WRN":                                                                       # conditie pentru "WRN"
            print(f"[WARNING] \nMesaj : {lista[1]} \nCod: {listb[1]}")

