lista = []

# Wprowadzanie ocen do listy
while True:
    ocena = input('Podaj ocene 2 - 5. Wpisz T lub t, by zakonczyc program: ')
    if ocena.upper() == 'T':
        break
    ocena = int(ocena)
    if ocena < 2 or ocena > 5:
        print('Podales nieprawidlowa ocene!')
    else:
        lista.append(ocena)

# Wyświetlanie listy
dlugoscListy = len(lista)
print(f'Wprowadzonych ocen: {dlugoscListy}')

# Sortowanie listy i jej wyświetlanie
lista.sort()
print('Lista: ', end='')
for i in range(dlugoscListy):
    if i == dlugoscListy - 1:
        print(lista[i], end='')
    else:
        print(lista[i], end=', ')
print()

# Ile razy występuje poszczególna ocena
for i in range(2, 6):
    if lista.count(i) == 1:
        print(f'{i}: {lista.count(i)} raz')
    else:
        print(f'{i}: {lista.count(i)} razy')

# Średnia ocen
print(f'Średnia ocen: {sum(lista)/dlugoscListy}')