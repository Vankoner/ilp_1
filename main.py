def sum_prime_divisors(n):
    """
    Функция 1: Находит сумму простых делителей числа.
    """
    if n <= 1:
        return 0

    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    divisors_sum = 0
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            divisors_sum += i

    return divisors_sum


# Тест функции
print("Тест функции sum_prime_divisors:")
print(f"sum_prime_divisors(30) = {sum_prime_divisors(30)}")