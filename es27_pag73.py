lista_veicoli=[]
while True:
    numero_veicoli_giornaliero=int(input("Scrivere numero veicoli: "))
    if numero_veicoli_giornaliero!=0:
        lista_veicoli.append(numero_veicoli_giornaliero)
    else:
        break
somma=0
for i in lista_veicoli:
    somma+=i
print("il totale dei veicoli transitati è : ", somma)