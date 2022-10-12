# 4. * Функция принимает в качестве аргументов строки в формате «Имя Фамилия»,
# возвращает словарь, ключи — первые буквы фамилий,
# значения — словари, реализованные по схеме предыдущего задания.

def first_name_last_name_dict(string):
    result_1 = {}
    for i in list(string):
        n, f = str(i).split(' ')    
        key_1 = f[0]
        if key_1 not in result_1:
            result_1[key_1] = []
        result_1[key_1].append(i)
    result_1 = dict(sorted(result_1.items(), key=lambda x: x[0]))
    for i in result_1:
        result_2 ={}       
        for k in result_1[i]:
            n, f = str(k).split(' ')    
            key_2 = n[0]
            if key_2 not in result_2:
                result_2[key_2] = []
            result_2[key_2].append(k)
        result_2 = dict(sorted(result_2.items(), key=lambda x: x[0]))
        result_1[i]=result_2
    return result_1

name = ("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                 "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
                 "Борис Аркадьев", "Антон Серов", "Павел Анисимов")
print(first_name_last_name_dict(name))
