partecipanti=int(input("quanti studenti ci sono in competizione? "))
valori=[]
for partecipanti in range(0,partecipanti):
    partecipanti-= 1
    print ("quanto ha lanciato? ")
    lancio = int(input())
    valori.append(lancio)
vincitore = max(valori)
print("il lancio vincente è stato di: ", vincitore, "metri")