# custom map(iterator), приймає dict і приймає 2 функції.
# Першу фунцію застосовуємо до ключів а другу до значень.
# map(dict, func1, funct2)
# (func1(key), func2(value))

def my_custom_map(my_dict, func1, func2):
    return {func1(key): func2(value) for key, value in my_dict.items()}


my_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
func1 = lambda x: x * 2
func2 = lambda x: x * 3

print(my_custom_map(my_dict, func1, func2))


