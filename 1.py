string_to_check = input("Inserisci parola: ")
if string_to_check == string_to_check[::-1]:
    print("La parola è palindroma")
else:
    print("La parola non è palindroma")