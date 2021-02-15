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