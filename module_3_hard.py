def structure_sum(data):
    full_sum = 0
    full_length = 0

    def recursive_helper(i):
        nonlocal full_sum, full_length

        if isinstance(i, (int, float)):
            full_sum += i
        elif isinstance(i, str):
            full_length += len(i)
        elif isinstance(i, (list, tuple, set)):
            for elem in i:
                recursive_helper(elem)
        elif isinstance(i, dict):
            for key, value in i.items():
                recursive_helper(key)
                recursive_helper(value)

    for element in data:
        recursive_helper(element)

    return full_sum + full_length


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = structure_sum(data_structure)
print(result)  # Должно выдать 99