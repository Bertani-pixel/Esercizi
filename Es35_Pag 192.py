#Organizza con un dizionario i dati sui conti correnti bancari con un numero del conto e saldo.
#Fornito poi il numero del conto, il programma visualizza il saldo oppure con un messaggio nel caso in cui il conto non sia presente sulla mappa

numero_conto = ["IT 12 L 12345 12345 123456789012", "IT 98 L 98765 98765 987654321098"]
saldo = ["2000 €", "400000 €"]
d = {}

for n in range(len(numero_conto)):
    d[numero_conto[n]] = saldo[n]

numero_conto_domanda = input("Di quale conto corrente desideri conoscere il saldo? ")
risposta = numero_conto_domanda.upper()

if risposta in numero_conto:
    print("Il saldo su questo conto è di:", d[risposta])
else:
    print("ERRORE: Il conto corrente inserito non è presente nella mappa!")