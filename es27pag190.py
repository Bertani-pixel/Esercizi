nomi={
    "Dario": "3454583502",
    "Giorgio": "8578682576",
    "Filippo": "7562738456",
    "Marco": "8310591365",
    "Luigi": "3940856093",
    "Francesco": "7086013475",
}

domanda=input("Scrivere il nome della persona di cui si vuole sapere il numero: ")
if domanda in nomi:
    print("Il numero di", domanda, "è:", nomi[domanda])
else:
    print("Questa persona non è presente nell'elenco")