# 2. Для чисел в пределах от 20 до N найти числа,
# кратные 20 или 21. Use comprehension.


def creat_list():
    n = input('Введите число больше 20: ')
    if n.isdigit():
        n = int(n)
        if n >= 20:
            lis = [i for i in range(20, n+1)]
            return lis
    print('Ошибка! Введён неверный размер списка.')
    return creat_list()


result = creat_list()
print(result)
result_list = [i for i in result if i % 20 == 0 or i % 21 ==0]
print(result_list)
