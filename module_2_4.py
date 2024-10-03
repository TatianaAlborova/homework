numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
def primes_(n):
    if n <= 1:                  # Проверка числа (простое или сложное):
        return False
    for i in range (2, int(n ** 0.5) + 1):      # Квадратный корень ускоряет процесс перебора делителей
        if n % i == 0:
            return False
    return True
for num in numbers:
    if primes_(num):
        primes.append(num)
    elif num > 1:
        not_primes.append(num)
print('Primes: ', primes)
print('Not primes: ', not_primes)