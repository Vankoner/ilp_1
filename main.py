def sum_prime_divisors(n):
    """ Функция 1: Находит сумму простых делителей числа."""
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

def count_odd_digits_greater_than_three(n):
    """Функция 2: Находит количество нечетных цифр числа, больших 3."""
    count = 0
    for digit in str(abs(n)):
        digit_int = int(digit)
        if digit_int % 2 != 0 and digit_int > 3:
            count += 1
    return count


def product_of_special_divisors(n):
    """Функция 3: Находит произведение делителей числа, сумма цифр которых меньше, чем сумма цифр исходного числа."""

    def digit_sum(x):
        return sum(int(digit) for digit in str(abs(x)))

    original_digit_sum = digit_sum(n)
    product = 1
    found_special_divisor = False

    for i in range(1, abs(n) + 1):
        if n % i == 0:
            if digit_sum(i) < original_digit_sum:
                product *= i
                found_special_divisor = True

    return product if found_special_divisor else 0


def test_functions():
    """Тестирование всех функций"""
    print("Тестирование функций:")
    print("_" * 100)

    # Тест 1
    num1 = 30
    print(f"Число: {num1}")
    print(f"1. Сумма простых делителей: {sum_prime_divisors(num1)}")
    print(f"2. Количество нечетных цифр > 3: {count_odd_digits_greater_than_three(num1)}")
    print(f"3. Произведение специальных делителей: {product_of_special_divisors(num1)}")
    print()

    # Тест 2
    num2 = 1234567
    print(f"Число: {num2}")
    print(f"1. Сумма простых делителей: {sum_prime_divisors(num2)}")
    print(f"2. Количество нечетных цифр > 3: {count_odd_digits_greater_than_three(num2)}")
    print(f"3. Произведение специальных делителей: {product_of_special_divisors(num2)}")
    print()

    # Тест 3
    num3 = 17
    print(f"Число: {num3}")
    print(f"1. Сумма простых делителей: {sum_prime_divisors(num3)}")
    print(f"2. Количество нечетных цифр > 3: {count_odd_digits_greater_than_three(num3)}")
    print(f"3. Произведение специальных делителей: {product_of_special_divisors(num3)}")


if __name__ == "__main__":
    test_functions()
