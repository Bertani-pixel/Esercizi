#Consegna Es14_Pag189
'''
Organizza in una struttura di dati i valori degli occupati negli ultimi dieci anni.
Utilizza un dizionario, assegnando il ruolo di chiave all'anno.
Inserisci i dati da tastiera e memorizzali nel contenitore.
Calcola poi il valore medio dei dieci anni e visualizzane il risultato.
'''

#Creazione dizionario vuoto
anni_dati={}

#Inserimento degli anni e dei valori
while True:
    anno=int(input("Scrivere l'anno (scrivere 0 per fermare): "))
    if anno==0:
        break
    else:
        dato=int(input("Scrivere il dato dell'anno inserito: "))
        anni_dati[anno]=dato

#Media dei valori
print("Questo è il valore medio di questi dieci anni:", sum(anni_dati.values())/len(anni_dati))