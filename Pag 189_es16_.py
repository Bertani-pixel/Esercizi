nazione = ["ITALIA", "SPAGNA", "FRANCIA", "INDIA", "CINA", "REGNO UNITO"]
capitale = ["Roma", "Madrid", "Parigi", "Nuova Delhi", "Pechino", "Londra"]
d = {}

for n in range(len(nazione)):
    d[nazione[n]] = capitale[n]

nazione_ = input("Di che nazione desideri sapere la capitale? ")
risposta = nazione_.upper()

if risposta in nazione:
    print(d[risposta])
else:
    print("ERRORE: la nazione che hai scritto non è presente nell'elenco!")