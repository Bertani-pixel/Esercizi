'''
Un'azienda vende prodotti in tutta Italia e la rete di vendita è suddivisa in quattro zone: Nord, Centro, Sud e Isole.
Dopo aver acquisito in un array il fatturato delle quattro zone, calcola:
- il totale del fatturato;
- i valori in percentuale delle vendite nelle quattro zone rispetto al totale.
'''

fatturati=[]

#Nord
Nord=int(input("Inserire il fatturato della zona Nord: "))
fatturati.append(Nord)

#Centro
Centro=int(input("Inserire il fatturato della zona Centro: "))
fatturati.append(Centro)

#Sud
Sud=int(input("Inserire il fatturato della zona Sud: "))
fatturati.append(Sud)

#Isole
Isole=int(input("Inserire il fatturato della zona Isole: "))
fatturati.append(Isole)

#Totale del fatturato
totale=sum(fatturati)
print("Il totale del fatturato è di", totale, "euro")

#Valori in percentuale
percentuale_Nord=Nord/totale*100
print("La percentuale del fatturato nella zona Nord rispetto al totale è del", percentuale_Nord, "%")

percentuale_Centro=Centro/totale*100
print("La percentuale del fatturato nella zona Centro rispetto al totale è del", percentuale_Centro, "%")

percentuale_Sud=Sud/totale*100
print("La percentuale del fatturato nella zona Sud rispetto al totale è del", percentuale_Sud, "%")

percentuale_Isole=Isole/totale*100
print("La percentuale del fatturato nella zona Isole rispetto al totale è del", percentuale_Isole, "%")