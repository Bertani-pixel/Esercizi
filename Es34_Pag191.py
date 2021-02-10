'''
Le prenotazioni per la partecipazione a un convegno sono memorizzate secondo l'ordine di arrivo. Scrivi un programma che comprenda due funzionalità:
- L'operazione per registrare i dati dei partecipanti;
- L'operazione per visualizzare i nomi dei partecipanti a cui si deve inviare una lettera di conferma: si tratta dei nomi dell'elenco,
  eliminando quelli ai quali la lettera è già stata inviata e che sono registrati in un apposito elenco. La funzione che produce l'elenco deve anche aggiornare l'elenco dei
  partecipanti ai quali è già stata inviata la lettera.
'''
prenotazioni_dati=[]
lettera_conferma_sì=[]
lettera_conferma_no=[]

while True:
    dati=input("Scrivere Nome e Cognome del partecipante: (Scrivere Fine per fermare) ")
    if dati=="Fine":
        break
    else:
        prenotazioni_dati.append(dati)
        conferma=input("Al partecipante deve essere inviata la lettera di conferma? ")
        if conferma=="Sì":
            lettera_conferma_sì.append(dati)
        elif conferma=="No":
            lettera_conferma_no.append(dati)

print("I partecipanti a cui si deve inviare la lettera di conferma sono: ", lettera_conferma_sì)