nazione = ["ITALIA", "SPAGNA", "FRANCIA", "INDIA", "CINA", "REGNO UNITO"]
capitale = ["Roma", "Madrid", "Parigi", "Nuova Delhi", "Pechino", "Londra"]

nazione_ = input("Di che nazione desideri sapere la capitale? ").upper()

if nazione_ in nazione:
    index = nazione.index(nazione_)
    print(capitale[index])
else:
    print("ERRORE: la nazione che hai scritto non è presente nell'elenco!")