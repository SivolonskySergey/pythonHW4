# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором
# повторение элементов списка будет прекращено.
from itertools import count
from itertools import cycle

user_list = [2, 4, 55, 8, 345, 0, 192]


def iterator_int(start, finish):
    for el in count(start):
        if el > finish:
            break
        else:
            print(el)


# iterator_int(5, 10)


def iterator_cycle(start_list, iter_amount):
    count = 0
    for el in cycle(start_list):
        if count > iter_amount:
            break
        print(el)
        count += 1

iterator_cycle(user_list, 30)

