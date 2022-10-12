# 5. ** Реализовать функцию, возвращающую n шуток,
# сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)

import random

def random_jokes(a, b, c, f, count):
    result=[]
    min_list = min(len(a), len(b), len(c))
    if f == 0 and count > min_list:
        for i in range(count):
            temp_word_1 = (random.choice(a))
            temp_word_2 = (random.choice(b))
            temp_word_3 = (random.choice(c))
            result.append(f'{temp_word_1} {temp_word_2} {temp_word_3}')
        return result
    else:
        if count > min_list:
            count = min_list
        for i in range(count):
            temp_word_1 = (random.choice(a))
            temp_word_2 = (random.choice(b))
            temp_word_3 = (random.choice(c))
            result.append(f'{temp_word_1} {temp_word_2} {temp_word_3}')
            a.remove(temp_word_1)
            b.remove(temp_word_2)
            c.remove(temp_word_3)
        return result

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра",
           "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

count_jokes = int(input('Введите количество шуток: '))
unique = int(input('Введите "1" для вывода уникальных шуток или введите "0" для вывода неуникальных шуток: '))
print(random_jokes(nouns, adverbs, adjectives, unique, count_jokes))
