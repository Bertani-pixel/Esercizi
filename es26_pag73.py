stipendio=float(input("Scrivere stipendio: "))
lista_stipendi=[]
while True:
    stipendio=int(input("Scrivere stipendio: "))
    if stipendio!=-1:
        lista_stipendi.append(stipendio)
    else:
        break
n=len(lista_stipendi)
somma=0
for i in lista_stipendi:
    somma+=i
media_stipendi=(somma)/n
print("La media è: ", media_stipendi)