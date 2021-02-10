a=int(input("Scrivi a: "))
b=int(input("Scrivi b: "))
if a==0:
    if b==0:
        print("Indeterminata")
    else:
        print("Impossibile")
else:
    if b==0:
        print("x = 0")
    else:
        print("x =", -(b/a))