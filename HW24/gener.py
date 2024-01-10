# написати свій генератор. Приймає int (кількість слів) а повертає рандомні слова.
#    Слова мають бути унікальні. Max int = 10_000.

import random

def unique_random_words(num):
    if num > 10_000:
        return "The number of words requested must be less then 10,000."

    list_of_words = open("D:\Hillel\Tasks\Стиль программирования Джо Селко на SQL.txt").readlines()
    random.shuffle(list_of_words)
    generated_words = set()

    for i in range(num):
        word = next(word for word in list_of_words if word not in generated_words)
        generated_words.add(word)
        yield word


for word in unique_random_words(100):
    print(word)


