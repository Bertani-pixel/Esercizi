'''
Acquisisci da tastiera un elenco di parole, memorizzandole in una lista,
finchè l'utente segnala la fine dell'inserimento con un asterisco *.
Visualizza alla fine il numero delle parole memorizzate.
Ordina alfabeticamente la lista delle parole e visualizzala,
ordinata in modo crescente o decrescente.
'''
lista=[]

while True:
    inserire=input("Inserire una parola (per fermare il tutto digitare '*'): ")
    if inserire=="*":
        break
    else:
        lista.append(inserire)

print("Sono state memorizzate", len(lista), "parole")
lista.sort()
print("Questi sono gli elementi della lista in ordine alfabetico:", lista)
lista.reverse()
print("Questi sono gli elementi della lista in ordine alfabetico decrescente:",lista)
