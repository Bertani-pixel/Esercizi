nazione = ["Italia", "Spagna", "Francia", "India", "Cina", "Regno Unito"]
capitale = ["ROMA", "MADRID", "PARIGI", "NUOVA DELHI", "PECHINO", "LONDRA"]
d = {}

for c in range(len(capitale)):
    d[capitale[c]] = nazione[c]

capitale_ = input("Di che capitale desideri sapere la nazione? ")
risposta = capitale_.upper()

if risposta in capitale:
    print(d[risposta])
else:
    print("ERRORE: la capitale che hai scritto non è presente nell'elenco!")