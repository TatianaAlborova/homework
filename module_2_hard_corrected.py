import random

first_number = random.randint(3, 20)

pairs = []

for i in range(1, 21):
    for j in range(i, 21):
        if i != first_number and j != first_number:
            pair_sum = i + j
            if first_number % pair_sum == 0:
                pairs.append((i, j))

if pairs:
    list_ = []
    for pair in pairs:
        list_.append(f'{pair[0]}{pair[1]}')
    result = ''.join(list_)
    print(f'{first_number} - {result}')
else:
    print("Нет подходящих пар чисел.")