'''
1 - Crea una classe 'Atleta' per rappresentare le informazioni su un giocatore. La classe deve contenere un attributo booleano chiamato 'visitaMedica'.
2 - Aggiungi alla classe 'Atleta' un metodo per assegnare all'atleta il nome della squadra dove gioca.
3 - Aggiungi alla classe 'Atleta' un metodo chiamato 'effettua_visita' che ponga l'attributo 'visitaMedica' uguale a 'True'.
4 - Agiungi alla classe 'Atleta' un metodo per visualizzare i dati del giocatore.
'''
class Atleta:
    def __init__(self, name, age, visitaMedica, squadra):
        self.name = name
        self.age = age
        self.visitaMedica = visitaMedica
        self.squadra = squadra

    def info(self):
        print("L'atleta si chiama", self.name)
        print("L'atleta ha", self.age, "anni.")

        if self.visitaMedica == True:
            print(self.name, "ha fatto la visita medica.")
        else:
            print(self.name, "non ha fatto la visita medica.")
        
        print(self.name, "gioca nella squadra", self.squadra + ".")
    
    def effetua_visita(self):
        self.visitaMedica = True

n1 = Atleta("Giorgio", 19, True, "Astralis")
n1.info()