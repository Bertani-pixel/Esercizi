scelta=input("Quale area vuoi calcolare? ")

if scelta=="Quadrato":
    lato=int(input("Scrivi il lato del quadrato: "))
    print("L'area del quadrato è ", lato*lato)

elif scelta=="Rettangolo":
    lato1=int(input("Scrivi il primo lato del rettangolo: "))
    lato2=int(input("Scrivi il secondo lato del rettangolo: "))
    print("L'area del rettangolo è: ", lato1*lato2)

elif scelta=="Triangolo":
    base=int(input("Scrivi la misura della base del triangolo: "))
    altezza=int(input("Scrivi la misura dell'altezza del triangolo: "))
    print("L'area del triangolo è: ", base*altezza)
    
elif scelta=="Cerchio":
    raggio=int(input("Scrivi la lungheza del raggio del cerchio: "))
    print("L'area del cerchio è ", raggio*raggio*3.14)