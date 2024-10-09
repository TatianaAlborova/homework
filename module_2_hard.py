import random

first_number = random.randint(3, 20)
print(f"Случайное число: {first_number}")

pairs = []

for i in range(1, 21):
    for j in range(1, 21):
        if i != first_number and j != first_number:
            pair_sum = i + j
            if first_number % pair_sum == 0:
                pairs.append((i, j))

if pairs:
    print("Подходящие пары чисел:")
    for pair in pairs:
        print(pair)
else:
    print("Нет подходящих пар чисел.")