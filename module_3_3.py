# 1 задание
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25, c = [1, 2, 3])

# 2 задание
def print_params(a, b, c):
    print(a, b, c)

values_list = [84.11, 'Текст', False]
values_dict = {'a': 44.38, 'b': 'Слово', 'c': False}

print_params(*values_list)
print_params(**values_dict)

# 3 задание
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)