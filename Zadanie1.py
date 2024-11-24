from random import randint

liczby = [randint(1, 100) for i in range(30)]

print(f'Parzyste: {[i for i in liczby if i % 2 == 0]}')
print(f'Nieparzyste: {[i for i in liczby if i % 2 != 0]}')