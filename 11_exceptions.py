


# terminalul are multiple stream-uri de text pe care le primeste si le afiseaza
#  STDERR e streamul de erori

print("==========:Inceput curs exceptii:==========")

lista1 = [9,10,11,33]

print(lista1)
print(lista1[3])



try:
    vari = int(input("De care index esti curios?\n"))
    print(lista1[vari])
    # exception is thrown from the int() conversion is caught asa ValueError
except IndexError:
    print("STOP RIGHT THERE CRIMINAL SCUM!")
except ValueError:
    print("You have to print an integer!")
# except BaseException:
#     print("YOU SHALL NOT PASS!!!")



# exception bubble-up

# var2 = int(input("Valoare var2:\n"))
#
# if var2 > 10:
#     raise Exception("Too high!")





print("==========:Sfarsit curs exceptii:==========")






















