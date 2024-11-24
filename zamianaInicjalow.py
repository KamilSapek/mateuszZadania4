def wypisz(tekst):
    for i in range(len(tekst)):
        if i != len(tekst) - 1:
            print(tekst[i], end='')
        else:
            print(tekst[i], end=' ')


imie = list('Stachu')
nazwisko = list('Mrozik')
n = nazwisko[0]
nazwisko[0] = imie[0]
imie[0] = n
wypisz(imie)
wypisz(nazwisko)