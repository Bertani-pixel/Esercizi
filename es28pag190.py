città_CAP={}

while True:
    città=input("Scrivere il nome della città (scrivere Fine per fermare): ")
    if città=="Fine":
        break
    else:
        CAP=input("Scrivere il CAP della città inserita: ")
        città_CAP[città]=CAP

domanda=input("Di che città vuoi sapere il CAP? ")
if domanda in città_CAP:
    print("Il CAP di", domanda, "è", città_CAP[domanda])
else:
    print("La città inserita non è presente nell'elenco")