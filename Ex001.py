# 1. Представлен список чисел.
# Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.


import random


def creat_rand_list():
    n = input('Введите размер списка: ')
    if n.isdigit():
        n = int(n)
        if n >= 0:
            lis = [random.randint(1, 10) for i in range(n)]
            return lis
    print('Ошибка! Введён неверный размер списка.')
    return creat_rand_list()


result = creat_rand_list()
print(result)
result_list = [k for i, k in zip(result, result[1:]) if i < k]
print(result_list)
