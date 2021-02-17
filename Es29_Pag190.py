'''
Scrivi un programma che legga un reddito da tastiera e calcoli l'importo dell'imposta sul reddito e la tassazione media.
Nell'esempio, per un reddito di 45.000 euro e un'imposta di 13.420 euro, la tassazione media è 13.420/45.000*100 = 29,82%.
Si nota che un reddito di 45.000 euro si colloca nella fascia limitata dal valore 55.000 e implica un'imposta di: 6960 + (45.000 - 28.000) * 38/100.
L'osservazione suggerisce di creare opportune strutture dati da utilizzare nel calcolo dell'imposta.
Per esempio si può pensare di creare un dizionario che associa al limite superiore di ogni fascia di reddito una tupla con:
limite inferiore della fascia, imposta dovuta per le fasce precedenti, aliquota della fascia.
Per trattare l'ultima fascia si introduce un limite superiore impossibile da raggiungere, come 10**12 (ovvero 1.000 miliardi).
'''

#Domanda del reddito
reddito=int(input("Scrivere il reddito: "))

#Ciclo if per trovare l'imposta
if reddito<=15000:
    imposta=reddito/100*23
    print("L'imposta è di", imposta, "euro")
elif 15000<reddito<=28000:
    imposta=(15000/100*23)+((reddito-15000)/100*27)
    print("L'imposta è di", imposta, "euro")
elif 28000<reddito<=55000:
    imposta=(15000/100*23)+(13000/100*27)+((reddito-28000)/100*38)
    print("L'imposta è di", imposta, "euro")
elif 55000<reddito<=75000:
    imposta=(15000/100*23)+(13000/100*27)+(27000/100*38)+((reddito-55000)/100*41)
    print("L'imposta è di", imposta, "euro")
elif 75000<reddito<10**12:
    imposta=(15000/100*23)+(13000/100*27)+(27000/100*38)+(20000/100*41)+((reddito-75000)/100*43)
    print("L'imposta è di", imposta, "euro")

#Calcolo della tassazione
tassazione=imposta/reddito*100
print("La tassazione è del", tassazione, "%")