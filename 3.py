while True:
    print("Parola italiana: ")
    parola=input()
    vocali=["a", "e", "i", "o", "u"]
    nuovaparola=""

    for i in parola:
        stato=vocali.count(i)
        if stato==0:
            index=parola.index(i)
            nuovaparola=nuovaparola+i+"o"+i
        else:
            nuovaparola=nuovaparola+i
            
    print("La nuova parola è: ", nuovaparola)
    print("Vuoi tradurre ancora? ")
    print("1 = Sì")
    print("2 = No")
    
    risposta=input()
    if risposta=="1":
        print("Benissimo!")
    else:
        break