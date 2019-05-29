import sys
import random

gracz = 0
komputer = 0

while True:

    # wybór gracza
    wybor = input("Wybierz figurę: \n(P)apier\n(K)amień\n(N)ożyce\n")
    wybor = wybor.upper()
    if wybor == "P":
        print("Gracz: Papier")
    elif wybor == "K":
        print("Gracz: Kamień")
    elif wybor == "N":
        print("Gracz: Nożyce")
    else:
        print("Wpisz: P, K lub N ")

    # wybór komputera
    wybor_komp = random.randrange(1, 4)

    if wybor_komp == 1:
        print("Komputer: Papier")
    elif wybor_komp == 2:
        print("Komputer: Kamień")
    elif wybor_komp == 3:
        print("Komputer: Nożyce")


    # sprawdzanie wyniku
    if wybor == "P" and wybor_komp == 2:
        print("Gracz wygrywa!")
        gracz += 1
    elif wybor == "K" and wybor_komp == 3:
        print("Gracz wygrywa!")
        gracz += 1
    elif wybor == "N" and wybor_komp == 1:
        print("Gracz wygrywa!")
        gracz += 1
    elif wybor == "K" and wybor_komp == 2:
        print("Komputer wygrywa!")
        gracz += 1
    elif wybor == "N" and wybor_komp == 2:
        print("Komputer wygrywa!")
        gracz += 1
    elif wybor == "P" and wybor_komp == 3:
        print("Komputer wygrywa!")
        komputer += 1

    if wybor == "P" and wybor_komp == 1:
        print("Remis!")
        gracz += 0
        komputer += 0
    elif wybor == "K" and wybor_komp == 2:
        print("Remis!")
        gracz += 0
        komputer += 0
    elif wybor == "N" and wybor_komp == 3:
        print("Remis!")
        gracz += 0
        komputer += 0

    # aktualny wynik
    print("Aktualny wynik: Gracz " + str(gracz) + ":" + str(komputer) + " Komputer")

    # pytanie o przedłużenie gry
    grasz_dalej = (input("Czy chcesz grać dalej? [t/n]: \n"))
    if grasz_dalej.lower() == "n":
        print("Exit")
        sys.exit(0)
