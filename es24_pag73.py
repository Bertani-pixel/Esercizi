voti_primo_candidato=int(input("Scrivere i voti del primo candidato: "))
voti_secondo_candidato=int(input("Scrivere i voti del secondo candidato: "))
percentuale_voti_primo_candidato=voti_primo_candidato/(voti_primo_candidato+voti_secondo_candidato)
print("percentuale voti primo candidato:", percentuale_voti_primo_candidato*100, "%")
percentuale_voti_secondo_candidato=voti_secondo_candidato/(voti_primo_candidato+voti_secondo_candidato)
print("percentuale voti secondo candidato:", percentuale_voti_secondo_candidato*100, "%")
if percentuale_voti_primo_candidato>percentuale_voti_secondo_candidato:
    print("Il primo candiato ha vinto!")
elif percentuale_voti_secondo_candidato==percentuale_voti_primo_candidato:
    print("Pareggio!")
else:
    print("Il secondo candidato ha vinto!")