nomi=[]
punti=[]
a=input("Inserisci il nome del primo candidato: ").upper()
num1=int(input("Inserisci il punteggio del primo candidato: "))
nomi.append(a)
punti.append(num1)
b=input("Inserisci il nome del secondo candidato: ").upper()
num2=int(input("Inserisci il punteggio del secondo candidato: "))
nomi.append(b)
punti.append(num2)
print("Elenco dei candidati in ordine alfabetico: ")
nomi.sort()
print(nomi)
input()
print("Elenco dei punteggi in ordine decrescente: ")
if num1>num2:
    print(num2, num1)
else:
    print(num1, num2)