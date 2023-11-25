from math import sqrt


def get_primes(numbers: list):
    for number in numbers:
        if number < 2:
            continue
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                break
        else:
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
