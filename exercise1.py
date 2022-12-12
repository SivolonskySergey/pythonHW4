# 1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, prod_in_hour, rate_in_hour, work_bonus = argv

print(f'выработка: {prod_in_hour}, ставка: {rate_in_hour}, премия: {work_bonus}')

def salary_count(prod, rate, bonus):
    result =  (int(prod) * int(rate)) + int(bonus)
    return f'Заработная плата сотрудника - {result}'

try:
    print(salary_count(prod_in_hour, rate_in_hour, work_bonus))
except ValueError:
    print('Пожалуйста, вводите только числа!')
