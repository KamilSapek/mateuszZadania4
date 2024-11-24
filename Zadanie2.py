from random import randint

liczby = [randint(1, 10) for i in range(5)]
liczby.sort()

wynik = 1

for i in liczby:
    wynik *= i

print(f'{liczby[0]}*{liczby[1]}*{liczby[2]}*{liczby[3]}*{liczby[4]}={wynik}')