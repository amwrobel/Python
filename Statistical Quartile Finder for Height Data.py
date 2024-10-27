def wczytaj_dane_do_tabeli(plik):
    """
    Wczytuje dane z pliku tekstowego do dwuwymiarowej listy.

    :param plik: Ścieżka do pliku z danymi
    :return: Lista dwuwymiarowa zawierająca dane
    """
    tabela = []  # Lista dwuwymiarowa na dane

    with open(plik, 'r') as f:
        for linia in f:
            # Usuwamy białe znaki i dzielimy po przecinku
            wiersz = linia.strip().split(',')  # Zakładamy, że dane są oddzielone przecinkiem
            tabela.append(wiersz)  # Dodajemy wiersz do tabeli
    
    return tabela

def oblicz_kwartyl(tabela, k):
    """
    Oblicza kwartyl na podstawie wczytanych danych.

    :param tabela: Dwuwymiarowa lista danych
    :param k: Numer kwartylu (1, 2, 3)
    """
    N = sum(int(wiersz[-1]) for wiersz in tabela)  # Suma wszystkich osób
    print("\nLiczba wszystkich danych:", N)
    
    Qwartyl = (k / 4) * N

    Numer_Osoby = 0  # Liczba osób do aktualnie rozpatrywanego kwartylu
    ostatni_wiersz = None  # Ostatnio przetwarzany wiersz
    Liczebnosc_ostatniego_przedzialu = 0
    Roznica_Przedzialow = 0
    Suma_poprzedzajacych_przedzialow = 0 

    # Sprawdzanie wierszy w celu znalezienia odpowiedniego przedziału
    for index, wiersz in enumerate(tabela):
        ostatni_wiersz = wiersz
        Numer_Osoby += int(wiersz[-1])
       
        if Numer_Osoby > Qwartyl:
            q = index + 1  # Numer przedziału
            print(f"\nQwartyl {k} to wzrost osoby o numerze: {int(Qwartyl)}, "
                  f"czyli znajduje się ona w przedziale wzrostu: {ostatni_wiersz[0]} - {ostatni_wiersz[1]}, "
                  f"numer przedziału: {q}")
            
            Liczebnosc_ostatniego_przedzialu = int(ostatni_wiersz[2])
            Roznica_Przedzialow = int(ostatni_wiersz[1]) - int(ostatni_wiersz[0])
            
            # Ustal sumę wartości w ostatniej kolumnie dla wierszy od 0 do q-1
            for i in range(q - 1):
                print(f'Wiersz {i + 1}:', tabela[i])  # Wyświetlenie wiersza
                Suma_poprzedzajacych_przedzialow += int(tabela[i][-1])  # Sumujemy wartość z ostatniej kolumny

            print("Suma poprzedzających przedziałów:", Suma_poprzedzajacych_przedzialow)
            break  # Zakończ pętlę po znalezieniu odpowiedniego przedziału

    # Informacje o zebranych danych
    print("\nZgromadzone dane:")
    print("Liczebnosc_ostatniego_przedzialu:", Liczebnosc_ostatniego_przedzialu)
    print("Roznica_Przedzialow:", Roznica_Przedzialow)
    print("Poczatek przedziału:", ostatni_wiersz[0])
    print("Koniec przedziału:", ostatni_wiersz[1])
    print("Obliczany kwartyl k =", k)
    print("N =", N)

    # Obliczanie wartości Q
    A = ((Qwartyl - Suma_poprzedzajacych_przedzialow) / Liczebnosc_ostatniego_przedzialu) * Roznica_Przedzialow
    Q = float(ostatni_wiersz[0]) + A

    print("\nKwartyl", k, "wynosi =", Q)


# Główna część programu
if __name__ == '__main__':
    plik = 'dane.txt'  # Nazwa pliku z danymi
    tabela = wczytaj_dane_do_tabeli(plik)

    k = 1  # Numer Kwartyla (1, 2, 3)
    oblicz_kwartyl(tabela, k)
