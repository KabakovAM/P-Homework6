# 3. Написать функцию, аргументы имена сотрудников,
# возвращает словарь, ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.


def names_dict(string):
    result = {}
    for i in list(string):
        k = i[0]
        if k not in result:
            result[k] = []
        result[k].append(i)
    result = dict(sorted(result.items(), key=lambda x: x[0]))
    return result

name = ("Иван", "Мария", "Петр", "Илья",
      "Марина", "Петр", "Алина", "Бибочка")
print(names_dict(name))
