import linecache
import sys

listaNat1 = []
listaNat2 = []
listaNatPlus12 = []

#################Funkcje wykonujące###############################

#Zliczanir ilości elementów wklejonych do notatników
def zliczNat(x):
    liczbaObiektow = -1
    for liczbaObiektow, zlicz in enumerate(x):
        pass
    liczbaObiektow += 1
    return liczbaObiektow

#Przepisanie elementów do listy
def PrzepiszLista(lista, plik, maxPozycja):
    element = 1
    while element < (maxPozycja + 1):
        wiersz = linecache.getline(plik, element)
        lista.append(wiersz)
        element += 1
    return lista

#Wyswietla wynik
def WypiszWynik(element, liczbaKorelacji):
    if element == 0:
        print("Nie znaleziono powiązań pomiędzy elemantami w plikach. \n")
    elif element == 1:
        if liczbaKorelacji < 5:
            print("Znaleziono " + str(liczbaKorelacji) + " korelacje pomiędzy plikami dla " + str(element) + " elementu.\n")
        else:
            print("Znaleziono " + str(liczbaKorelacji) + " korelacji pomiędzy plikami dla " + str(element) + " elementu:\n")

    else:
        if liczbaKorelacji < 5:
            print("Znaleziono " + str(liczbaKorelacji) + " korelacje pomiędzy plikami dla " + str(element) + " elementów.\n")
        else:
            print("Znaleziono " + str(liczbaKorelacji) + " korelacji pomiędzy plikami dla " + str(element) + " elementów.\n")

def MenuGlowne():
    print("Wybierz działanie:\n")
    print("1 - Instrukcja")
    print("2 - Uruchom program")
    print("9 - O programie")
    print("0 - Wyjście z programu\n")

def ObslugaMenuGlowne():
    MenuGlowne()
    while True:
        dzialanie = int(input())
        if dzialanie == 0:
            sys.exit()
        elif dzialanie == 1:
            man = open("pliki/Manual.txt", 'r', encoding='utf-8')
            print(man.read() + "\n")
            man.close()
            MenuGlowne()
            continue
        elif dzialanie == 2:
            print("Uruchamianie programu...\n")
            break
        elif dzialanie == 9:
            print("natRAY\n" + "Wersja 1.0\n" + "Autor: Kamil Kołodziejczyk\n" + "Emial: zaurish@op.pl\n")
            print("Wszelkie zmiany w kodzie bez zgody autora zabronione!\n")
            MenuGlowne()
            continue
        else:
            MenuGlowne()
            continue


#################################################################
print("natRAY\n" + "Wersja 0.1\n")
print("Witaj w programie natRay\n")
ObslugaMenuGlowne()

liczbaObiektow1 = zliczNat(open('nat1.txt', 'r'))
print("Plik nat1.txt zawiera " + (str(liczbaObiektow1)) + " pozycji.")
liczbaObiektow2 = zliczNat(open('nat2.txt', 'r'))
print("Plik nat2.txt zawiera " + (str(liczbaObiektow2)) + " pozycji.\n")
#liczbaObiektow3 = zliczNat(open('nat3.txt', 'r'))
#print("Trzeci plik zawiera " + (str(liczbaObiektow3)) + " pozycji.\n")

listaNat1 = PrzepiszLista(listaNat1, 'nat1.txt', liczbaObiektow1)
listaNat2 = PrzepiszLista(listaNat2, 'nat2.txt', liczbaObiektow2)
#listaNat3 = PrzepiszLista(listaNat3, 'nat3.txt', liczbaObiektow3)
#print(listaNat1)
#print(listaNat2)
#print(listaNat3)

i = 0
j = 0
element = 0 # licznik elementów w liście wynikowej
plik = open('wynik.txt', 'w') #otwarcie pliku wynikowego
while i < (liczbaObiektow1):
    while j < (liczbaObiektow2):
        a = listaNat2[j]
        if a in listaNat1:
            if a not in listaNatPlus12:
                plik.write(str(a))
                element += 1
            listaNatPlus12.append(a)
        j += 1
    i += 1
plik.close()
liczbaKorelacji = len(listaNatPlus12)

if element == 0:
    WypiszWynik(element, liczbaKorelacji)
    print("Naciśnięcie dowolnego klawisza spowoduje zakończenie pracy programu...")
else:
    WypiszWynik(element, liczbaKorelacji)
    print("W obu plikach znaleziono następujące obiekty:\n")
    wyn = open("wynik.txt", 'r')
    print(wyn.read())
    wyn.close()
    print('Powyższe pozycje zostały zapisane w pliku "wynik.txt".\n')
    print("Naciśnięcie klawisza Enter spowoduje zakończenie pracy programu...")

input()
