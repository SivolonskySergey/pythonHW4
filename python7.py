from itertools import count

def fact(n):
    factor = 1
    for x in count(1):
        if x > n:
            break
        factor = factor * x
        yield factor

n = int(input('Введите максимальное положительное значение: '))
i = 0

for el in fact(n):
    i += 1
    print(f'факториал {i} = {el}')